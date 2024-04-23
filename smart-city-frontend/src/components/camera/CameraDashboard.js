import React, { useEffect, useState } from 'react';
import { Container, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Typography, TextField } from '@material-ui/core';

function CameraDashboard() {
  const [cameras, setCameras] = useState([]);
  const [search, setSearch] = useState('');

  useEffect(() => {
    // Fetch the camera data from your API
    fetch('/cameras')
      .then(response => response.json())
      .then(setCameras)
      .catch(error => console.error('Error:', error));
  }, []);

  const filteredCameras = cameras.filter(camera => camera.name.toLowerCase().includes(search.toLowerCase()));

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
              <TableRow key={camera.id}>
                <TableCell component="th" scope="row">
                  {camera.name}
                </TableCell>
                <TableCell align="right">{camera.latitude}</TableCell>
                <TableCell align="right">{camera.longitude}</TableCell>
                <TableCell align="right">{camera.inService ? 'Yes' : 'No'}</TableCell>
                <TableCell align="right">{camera.streamingUrl}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Container>
  );
}

export default CameraDashboard;