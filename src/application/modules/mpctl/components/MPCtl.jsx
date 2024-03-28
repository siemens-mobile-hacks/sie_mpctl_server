import React, { useState, useEffect } from 'react';
import { useWebSocket } from '~/hooks/websocket';
import Typography from "@mui/material/Typography/Typography";
import Volume from '../components/Volume';
import Controls from '../components/Controls';
import Track from './Track/Track';
import '../styles/MPCtl.scss';

const MPCtl = () => {
    const [data, setData] = useState({connected: false});

    const wsData = useWebSocket('/ws/data/', {
        shouldReconnect: () => true,
    });

    useEffect(() => {
        if (wsData.lastJsonMessage) {
            setData(wsData.lastJsonMessage);
        }
    }, [wsData.lastJsonMessage]);

    const handleClickCtlButton = (action) => () => {
        wsData.sendMessage(action);
    };

    return (
        <div id="MPCtl">
            {(data.connected)
                ? <>
                    {(data.status >= 0)
                        ? <Volume onClick={handleClickCtlButton}/>
                        : null
                    }
                    <Track track={data.track} status={data.status}/>
                    <Controls onClick={handleClickCtlButton}/>
                </>
                : <div className="not-connected">
                    <Typography color="error">
                        Not connected!
                    </Typography>
                </div>
            }
        </div>
    );
};

export default MPCtl;
