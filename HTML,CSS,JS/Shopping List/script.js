const list = document.querySelectorAll("ul");
const listItem = document.querySelectorAll("li"); // check if correct
const input = document.querySelector("input");
const title = document.querySelector("h3");
const addListButton = document.querySelector(".add-list-button");
const addItemButton = document.querySelector(".add-item-button");
const deleteListButton = document.querySelector(".delete-list-button");
const deleteItemButton = document.querySelector(".delete-item-button");

// ADD LIST BUTTON + CLONE TEMPLATE

addListButton.addEventListener("click", function() {
    const inputValue = inputField.value;
    const template = document.getElementById("itemTemplate");
    const clone = template.content.cloneNode(true);

    // Check if the input value is not empty
    if (inputValue.trim() !== '') {
        alert("Please enter a name for the list.");
    
    clone.querySelector(".list-category").textContent = userInputValue;
    document.getElementById("container").appendChild(clone);

});


// DELETE LIST BUTTON
deleteListButton.addEventListener('click', () => {
    list.remove(); // make sure this targets only ONE SPECIFIC list
    alert("Div removed!"); // or innerText to put this on HTML? create a place to show this though
});


// DELETE ITEM BUTTON
deleteItemButton.addEventListener('click', () => {
    list-item.remove(); // make sure this targets only ONE SPECIFIC list
    alert("Div removed!"); // or innerText to put this on HTML? create a place to show this though
});


/*
SPECIFIC LIST HTML CONTENT

<div class="list">
    <h3 class="list-category"></h3>>
    <input type="text" id="new-item" placeholder="Enter an item..." />
    <button class="add-item-button">Add Item</button>
    <ul></ul>
</div>
*/

// ADD ITEM TO LIST BUTTON 

addItemButton.addEventListener("click", function() {
    const inputValue = inputField.value;

    // Check if the input value is not empty
    if (inputValue.trim() !== '') {
        const newListItem = document.createElement('li');

        newListItem.textContent = inputValue;

        // Append the new list item to the unordered list
        list[].appendChild(newListItem); // use indices to target specific list?

        // Clear the input field
        inputField.value = '';
    input.textContent = "";

import React, { useState, useRef } from 'react';
import './App.css';
/*
import mySong from './Coding/React/first-project/Lukrembo.mp3';
*/


// FROM REACT, CHANGE TO JS
export default function App() {

  };
  
  document.addEventListener('DOMContentLoaded', function() {
    const myInput = document.getElementById('task-input');
    const addTaskButton = document.getElementsByClassName('add-button');

    addTaskButton.addEventListener('click', function() {

      const addTask = () => {
        var newList = document.createElement('li');
        var task = document.createElement('span');
        var deleteTaskButton = document.createElement('button');
        var inputValue = myInput.value;

        newList.classList.add('task-item');
        task.textContent = inputValue;
        deleteButton.textContent = "X";
        deleteButton.classList.add('delete-button');
        deleteButton.onclick = deleteTask;

        newList.appendChild(task);
        newList.appendChild(deleteButton);
      };
    });

    deleteTaskButton.addEventListener('click', function() {

      const deleteTask = () => {
        var taskToRemove = event.target.parentNode; 
        taskToRemove.remove();
        task.remove();
        deleteButton.remove();
      };
  });
  

  return (
    <div className="container">
      <h1>To-Do List</h1>

      <div className="input-group">
        <input id="task-input" type="text" placeholder="Enter a task" />
        <button className="add-button" type="submit" onClick={addTask}>Add</button>
      </div>

      <ul>
        <li className="task-item">
          <span>Wash the dishes</span>
          <button className="delete-button" onClick={() => deleteTask(index)}>X</button>
      </li>
      </ul>
    </div>

    );
  });
}



ADD LIST BUTTON
- If no input, do not go through 
- Create new list template below
- H1 name should change to inputted value (text content)
= may need to assign class to input & rename
- (CSS) align list below, margin as 0 auto;

ADD ITEM BUTTON
- create new li element
- change text content to input
- add delete button to side of name