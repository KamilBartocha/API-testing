// Tests 
// Status code check
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// Status response check
const response = pm.response.json();
console.log(response.status);
console.log(response['status']);

// pm.test("1 should be 1", () => {
//     pm.expect(1).to.eql(1)
// });

pm.test("Status should be OK", () => {
    pm.expect(response.status).to.eql("OK")
});

// Runner setting next Request after executing this one
postman.setNextRequest("List of books");
postman.setNextRequest(null) // STOP execution

//-------------------------------------------------------------------//

// Filtering response and check if parameter is set to desire value
const response = pm.response.json();
const nonFictionBooks = response.filter((book) => book.available === true);
console.log(nonFictionBooks[0].id);

// Check if book from response is "correct"

const book = nonFictionBooks[0];
// pm.globals.set("bookId", nonFictionBooks[0].id);
if(book) {
    pm.globals.set("bookId", book.id);
}
pm.test("Book found", () => {
    pm.expect(book).to.be.an('object');
    pm.expect(book.available).to.be.true;
    pm.expect(book.available).to.eql(true);
})
pm.test("Book not-fiction", () => {
    pm.expect(book.type).to.eql("non-fiction")
});

//-------------------------------------------------------------------//

// Check if books amount is grater than 0 

// pm.test("Is in stock", () => {
//     pm.expect(1).to.be.above(2);
// });
 
const response = pm.response.json()
pm.test("Is in stock", () => {
    pm.expect(response["current-stock"]).to.be.above(0)
})

// Set global var - orderID

const response = pm.response.json();

pm.globals.set("orderId", response.orderId);
