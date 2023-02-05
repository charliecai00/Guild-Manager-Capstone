import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }


const App = ({ word }) => {
  const [guess, setGuess] = useState('')
  const [guesses, setGuesses] = useState([])
  const [correctGuess, setCorrectGuess] = useState(false)

  const handleGuess = evt => {
    setGuesses(prevGuesses => [...prevGuesses, guess])
    setGuess('')
    if(guess === word) {
      setCorrectGuess(true)
    }
  }

  const handleChange = evt => {
    setGuess(evt.target.value)
  }

  const wordArr = [...word]
  const guessElements = guesses.map(w => {
    return <Guess key={w} guess={[...w]} secret={wordArr} /> 
  })

  let guessForm = (
    <GuessForm 
        handleGuess={handleGuess} 
        handleChange={handleChange}
        value={guess}
    />)

  return (
    <div className="game">
      <h2>Wordle Wide Web</h2>
      {guessElements}
      {correctGuess ? <h2>Correct!</h2> : guessForm}
    </div>
  )
}

const GuessForm = ({ handleGuess, handleChange, value }) => {
  return (
    <>
    <input type="text" value={value} onChange={handleChange} />
    <button onClick={handleGuess}>Guess</button>
    </>
  )
}

const Guess = ({ guess, secret }) => {
  const letters = guess.map((letter, i) => {
    return (
      <div key={letter+i} className={letter === secret[i] ? 'match': 'unmatch'}>
        {letter}
      </div>
    )
  })
  return (
    <div className='word'>
      { letters } 
    </div>
  ) 
}

export default App;
