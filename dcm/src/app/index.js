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
        console.log(fetch("http://localhost:8000/dcm/api/list/"))
        fetch("http://localhost:8000/dcm/api/list/", {
            mode: "no-cors",
            method: 'GET',
            headers: {
                Accept: 'application/json',
            },
        },)
            .then(res => res.json())
            .then(result =>
                this.setState({
                    isLoaded: true,
                    containers: result.tag
                })
            )
            .catch(error =>
                this.setState({
                    isLoaded: true,
                    error
                })
            );
    }

    render() {
        const {error, isLoaded, containers} = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading ...</div>;
        } else {
            return (
                <ul>
                    {containers}
                    {/*{containers.map(item => (*/}
                    {/*<li key={item.container_id}>*/}
                    {/*{item.container_id} {item.status}*/}
                    {/*</li>*/}
                    {/*))}*/}
                </ul>
            );
        }
    }
}

render(<App/>, window.document.getElementById("app"));