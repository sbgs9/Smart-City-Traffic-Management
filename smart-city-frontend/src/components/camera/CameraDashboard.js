import React, { useEffect, useState } from 'react';
import { Container, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Typography, TextField, Collapse } from '@material-ui/core';

function CameraDashboard() {
  const [cameras, setCameras] = useState([]);
  const [search, setSearch] = useState('');
  const [open, setOpen] = useState({});
  const [error, setError] = useState({});

  useEffect(() => {
    fetch('/cameras')
      .then(response => response.json())
      .then(setCameras)
      .catch(error => console.error('Error:', error));
  }, []);

  const filteredCameras = cameras.filter(camera => camera.name.toLowerCase().includes(search.toLowerCase()));

  const handleClick = (id) => {
    setOpen(prevOpen => ({ ...prevOpen, [id]: !prevOpen[id] }));
  };

  const handleVideoError = (id) => {
    setError(prevError => ({ ...prevError, [id]: true }));
  };

  return (
    <Container>
      <Typography variant="h4" component="h1" gutterBottom>
        CCTV Camera Dashboard
      </Typography>
      <TextField
        label="Search"
        variant="outlined"
        value={search}
        onChange={e => setSearch(e.target.value)}
      />
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell align="right">Latitude</TableCell>
              <TableCell align="right">Longitude</TableCell>
              <TableCell align="right">In Service</TableCell>
              <TableCell align="right">Streaming URL</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {filteredCameras.map((camera) => (
              <React.Fragment key={camera.id}>
                <TableRow onClick={() => handleClick(camera.id)}>
                  <TableCell component="th" scope="row">
                    {camera.name}
                  </TableCell>
                  <TableCell align="right">{camera.latitude}</TableCell>
                  <TableCell align="right">{camera.longitude}</TableCell>
                  <TableCell align="right">{camera.inService ? 'Yes' : 'No'}</TableCell>
                  <TableCell align="right">{camera.streamingUrl}</TableCell>
                </TableRow>
                <TableRow>
                  <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
                    <Collapse in={open[camera.id]} timeout="auto" unmountOnExit>
                      {error[camera.id] ? (
                        <p>Stream Unavailable</p>
                      ) : (
                        <iframe title="Camera Stream" src={camera.streamingUrl} width="200" height="150" allow="autoplay"></iframe>
                      )}
                      <img src={camera.streamingUrl} style={{ display: 'none' }} onError={() => handleVideoError(camera.id)} alt="" />
                    </Collapse>
                  </TableCell>
                </TableRow>
              </React.Fragment>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Container>
  );
}

export default CameraDashboard;