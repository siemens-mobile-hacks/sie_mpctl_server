import React from 'react';
import PropTypes from 'prop-types';
import IconButton from '@mui/material/IconButton';
import AddIcon from '@mui/icons-material/Add';
import RemoveIcon from '@mui/icons-material/Remove';

const Volume = ({onClick}) => {
    return (
        <div className="volume">
                <IconButton size="large" onClick={onClick('vol-down')}>
                    <RemoveIcon/>
                </IconButton>
                <IconButton size="large" onClick={onClick('vol-up')}>
                    <AddIcon/>
                </IconButton>
            </div>
    );
};

Volume.propTypes = {
    onClick: PropTypes.func.isRequired,
};

export default Volume;
