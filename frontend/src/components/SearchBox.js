import React, { useState } from "react";

/* REACT BOOTSTRAP */
import { Button, Form } from "react-bootstrap";

/* REACT ROUTER DOM */
import { useHistory } from "react-router-dom";

function SearchBox() {
  /* STATE */
  const [keyword, setKeyword] = useState("");

  let history =
    useHistory(); /* CAN'T DIRECTLY USE HISTORY AS IT'S NOT AN ACTUAL PAGE SO CAN'T DESTRUCTURE PROPS */

  /* HANDLER */
  const submitHandler = (e) => {
    e.preventDefault();

    // WHEN USER HITS SUBMIT, REDIRECT TO HOME PAGE TO SEE PRODUCTS AND APPEND ?keyword=...IN URL
    if (keyword) {
      history.push(`/?keyword=${keyword}&page=1`);
    } else {
      // IF WE HIT SUBMIT WITHOUT KEYWORD, WE DON'T WANT THE USER TO GET REDIRECTED IN THAT CASE RATHER STAY ON WHATEVER PAGE HE WAS
      history.push(history.push(history.location.pathname));
    }
  };

  return (
    <Form onSubmit={submitHandler} className="d-flex">
      <Form.Control
        style={{width:"250px" ,borderRadius:"5px" ,color:"Blue Yonder", backgroundColor: "Blue Yonder"}}
        type="text"
        name="q"
        placeholder="Search"
        backgroundColor= "Blue Yonder"
        color="Blue Yonder"
        onChange={(e) => setKeyword(e.target.value)}
        className="mr-sm-2 ml-sm-5"
      ></Form.Control>
      <Button type="submit" 
        variant="outline-Info" className="p-2 mx-sm-2"
      >
        Search
      </Button>
    </Form>
  );
}

export default SearchBox;
