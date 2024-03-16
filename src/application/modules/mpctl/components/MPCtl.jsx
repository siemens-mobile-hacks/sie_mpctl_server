import React, { useEffect } from 'react';
import { useWebSocket } from '~/hooks/websocket';
import Typography from '@mui/material/Typography';
import IconButton from "@mui/material/IconButton";
import AddIcon from '@mui/icons-material/Add';
import StopIcon from '@mui/icons-material/Stop';
import RemoveIcon from '@mui/icons-material/Remove';
import SkipNextIcon from '@mui/icons-material/SkipNext';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import SkipPreviousIcon from '@mui/icons-material/SkipPrevious';
import '../styles/MPCtl.scss';

const MPCtl = () => {
    const wsData = useWebSocket('/ws/data/', {
        shouldReconnect: () => true,
    });

    useEffect(() => {
        console.log('get:', wsData.lastJsonMessage);
    }, [wsData.lastJsonMessage]);

    return (
        <div id="MPCtl">
            <div className="volume">
                <IconButton size="large">
                    <RemoveIcon/>
                </IconButton>
                <Typography size="small">10</Typography>
                <IconButton size="large">
                    <AddIcon/>
                </IconButton>
            </div>
            <Typography className="song">Name of song</Typography>
            <div className="controls">
                <IconButton size="large">
                    <SkipPreviousIcon/>
                </IconButton>
                <IconButton size="large">
                    <PlayArrowIcon/>
                </IconButton>
                <IconButton size="large">
                    <StopIcon/>
                </IconButton>
                <IconButton size="large">
                    <SkipNextIcon/>
                </IconButton>
            </div>
        </div>
    );
};

export default MPCtl;
