import use from 'react-use-websocket';

export function useWebSocket (path, options) {
    const protocol = (location.protocol === 'http:') ? 'ws:' : 'wss:';
    const url = `${protocol}//${location.hostname}:${location.port}${path}`;
    return use(url, options);
}
