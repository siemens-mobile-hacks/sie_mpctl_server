import React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import MPCtl from '@/modules/mpctl/components/MPCtl';
import '../styles/Application.scss';

const darkTheme = createTheme({
    palette: {
        mode: 'dark',
    },
});

const Application = () => {
    return (
        <ThemeProvider theme={darkTheme}>
            <CssBaseline/>
            <div>
                <MPCtl/>
            </div>
        </ThemeProvider>
    );
};

export default Application;
