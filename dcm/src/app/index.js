import React from "react";
import {render} from "react-dom";

class App extends React.Component {
    constructor(props) {
        super();
        this.state = {
            error: null,
            isLoaded: false,
            containers: []
        };
    }

    componentDidMount() {
        fetch("http://localhost:8000/dcm/api/list/", {
            mode: 'no-cors',
            method: 'GET',
            dataType: 'json',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        })
            .then(response => response.json())
            .then(response => {
                this.setState({
                    isLoaded: true,
                    containers: response
                });
            })
            .catch(error =>
                this.setState({
                    isLoaded: true,
                    error
                })
            );
    }

    render() {
        const {error, isLoaded} = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading ...</div>;
        } else {
            const containers = this.state.containers.map((container) =>
                <div key={container.container_id}>
                    <p>container_id: {container.container_id}</p>
                    <p>tag: {container.tag}</p>
                    <p>image: {container.image}</p>
                    <p>image_id: {container.image_id}</p>
                    <p>command: {container.command}</p>
                    <p>created: {container.created}</p>
                    <p>status: {container.status}</p>
                    <p>state: {container.state}</p>
                    <p>ports: {container.ports}</p>
                    <p>names: {container.names}</p>
                    <p>ip: {container.ip}</p>
                    <hr/>
                </div >);

            return (
                <div>{containers}</div>
            );
        }
    }
}

render(<App/>, window.document.getElementById("app"));