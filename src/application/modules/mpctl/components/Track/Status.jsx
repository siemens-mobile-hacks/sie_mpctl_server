import React from 'react';
import PropTypes from 'prop-types';
import StopIcon from '@mui/icons-material/Stop';
import PauseIcon from '@mui/icons-material/Pause';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';

const Status = ({status}) => {
    switch (status) {
        case 0:
            return <StopIcon/>;
        case 1:
            return <PauseIcon/>;
        case 2:
            return <PlayArrowIcon/>;
    }
    return <></>;
};

Status.propTypes = {
    status: PropTypes.number.isRequired,
};

export default Status;
