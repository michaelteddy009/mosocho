// EXAMINE THE DOCUMENT

console.dir(document); // from these we cn log other things like .domain, .URL, 
console.log(document.title);

// we can even make  change
document.title = 'new';

// to access the inner elements
var firstTitle = document.getElementById('');
firstTitle.textContent = 'new head';
firstTitle.innerText = 'latest head';
firstTitle.innerHTML = '<h1>the min pge</h1>'

//change the style using carmel case
firstTitle.style.boarderBottom()

//get elements by class names
var items = document.getElementsByClassName('item-list')

//get element by tag name
var li = document.getElementByTagName() 

// Queryselector //
var header = document.querySelector('#main-header')
header.style.boarderBottom = 'solid 4px grey'

var input = document.querySelector('input[type='submit']')
input.value = 'hello world'

var nother = document.querySelector('.iten-list:nth-child(2)')
nother.style.color('red')

// query selectorAll will work just like tag and class name


