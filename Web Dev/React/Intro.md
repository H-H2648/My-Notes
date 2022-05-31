# Intro to React

Note based on [turtorial](https://reactjs.org/turtorial/turtorial.html)

## Starting React Applications

To start a React code:

`npx create-react-app {NAME_OF_APPLICATION}`

Important import:

```
import React from "react";
import ReactDOM from "react-dom/client";
```

## Components

Consists of independent pieces called **components** that compose to form complex UI. To declare component:

```
class SomeComponent extends React.Component {
    render() {
        return (
            <div className="SomeComponentName">
                // some code for displaying the component
            </div>
        )
    }
}
```

Components takes in parameters called `props` (properties) and returns some "views" for dispaying application via the `render` method

## Passing Value between Components

Two components can pass values between each other. For example the class `A` may have a method:

```
class A extends React.Component {
    renderB(ii){
        return <B value={ii} test="test">
    }
}
```

Note calling `<B >` allows us to render the React component `B` using the component `A`. Note that putting value={ii} and test="test" assigns the `prop` value of the component `B` of `prop.value=ii`, `prop.test="test"`. So we may declare our class `B` like:

```
class B extends React.Component {
    render() {
        return (
            <h1>Value: {this.props.value}</h1>
            <button 
                className="button
                onClick={() => console.log("The button has been clicked")}
            >
                {this.props.test}
            </button>
        )
    }
}
```

## Interactive Components

Note that we can make our component interactive. This introduces us to `state`. To declare state, we must always call `constructor` on `props`. To make the component interactive, we keep track of its state as it changes:

```
class B extends React.Component {
    constrctor(props){
        super(props);
        this.state ={
            value: null,
        }
    }
    render() {
        return (
            <h1>Value: {this.props.value}</h1>
            <button 
                className="button
                onClick={() => this.setState({value:"not null"})}
            >
                {this.props.test}
            </button>
        )
    }
}
```

Note that `super(props)` is necessary.

## Functional Components

Note that for our example above for class `SomeComponent`, it only has one method of `render()`. This can be replaced with a functional component:

```
function SomeComponent(props){
    return (
        <div className="SomeComponentName">
            // some code for displaying the component
        </div>
    )
}
```
