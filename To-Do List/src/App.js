import React from 'react';
import './App.css';

function App() {

  return (
    <div className="container">
      <h1>To-Do List</h1>

      <div className="input-group">
        <input type="text" placeholder="Enter a task" />
        <button className="add-button" type="submit">Add</button>
      </div>

      <ul>
        <li className="task-item">
          <span>Wash the dishes</span>
          <button className="delete-button">X</button>
      </li>
      </ul>
    </div>
    /*
    const MusicPlayer = () => {
      <div>
        <audio controls src="" />
        <p>Now playing: Your Awesome Song</p>
      </div>
      */
    };
  )
}

export default App;
