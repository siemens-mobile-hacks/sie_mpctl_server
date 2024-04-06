import React from 'react';
import PropTypes from 'prop-types';
import IconButton from '@mui/material/IconButton';
import StopIcon from '@mui/icons-material/Stop';
import PauseIcon from '@mui/icons-material/Pause';
import CloseIcon from '@mui/icons-material/Close';
import SkipNextIcon from '@mui/icons-material/SkipNext';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import SkipPreviousIcon from '@mui/icons-material/SkipPrevious';

const Controls = ({onClick}) => {
    return (
        <div className="controls">
            <IconButton size="large" onClick={onClick('prev')}>
                <SkipPreviousIcon/>
            </IconButton>
            <IconButton size="large" color="success" onClick={onClick('play')}>
                <PlayArrowIcon/>
            </IconButton>
            <IconButton size="large" color="warning" onClick={onClick('pause')}>
                <PauseIcon/>
            </IconButton>
            <IconButton size="large" color="error" onClick={onClick('stop')}>
                <StopIcon/>
            </IconButton>
            <IconButton size="large" onClick={onClick('next')}>
                <SkipNextIcon/>
            </IconButton>
            <IconButton size="large" color="error" onClick={onClick('kill')}>
                <CloseIcon/>
            </IconButton>
        </div>
    );
};

Controls.propTypes = {
    onClick: PropTypes.func.isRequired,
};

export default Controls;
