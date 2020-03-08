package main

import (
	"log"
	"net/http"

	_ "github.com/gorilla/mux"
)

func setupRouter(router *mux.Router) {
	router.
		Methods("POST").
		Path("/endpoint").
		HandlerFunc(postFunction)
}

func postFunction(w http.ResponseWriter, r *http.Request) {
	database, err := db.CreateDatabase()
	if err != nil {
		log.Fatal("Database connection failed")
	}

	_, err = database.Exec("INSERT INTO `test` (name) VALUES ('myname')")
	if err != nil {
		log.Fatal("Database INSERT failed")
	}
	
	log.Println("You called a thing!")
}

func main() {
	router := mux.NewRouter().StrictSlash(true)

	setupRouter(router)

	log.Fatal(http.ListenAndServe(":8080", router))
}