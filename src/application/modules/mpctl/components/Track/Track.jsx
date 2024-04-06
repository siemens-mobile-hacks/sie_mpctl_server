import React from 'react';
import PropTypes from 'prop-types';
import Typography from '@mui/material/Typography/Typography';
import Status from './Status';

const Track = (props) => {
    return (
        <div className="track">
            {(props.status >= 0)
                ? <div>
                    <Status status={props.status}/>
                    <Typography>{props.track}</Typography>
                </div>
                : <Typography color="error">Media player is not running!</Typography>
            }
        </div>
    );
};

Track.propTypes = {
    track: PropTypes.string,
    status: PropTypes.number.isRequired,
};

export default Track;
