import React, { useEffect } from 'react';
import { useWebSocket } from '~/hooks/websocket';
import Volume from '../components/Volume';
import Controls from '../components/Controls';
import '../styles/MPCtl.scss';

const MPCtl = () => {
    const wsData = useWebSocket('/ws/data/', {
        shouldReconnect: () => true,
    });

    useEffect(() => {
    }, [wsData.lastJsonMessage]);

    const handleClickCtlButton = (action) => () => {
        wsData.sendMessage(action);
    };

    return (
        <div id="MPCtl">
            <Volume onClick={handleClickCtlButton}/>
            <Controls onClick={handleClickCtlButton}/>
        </div>
    );
};

export default MPCtl;
