package main

import (
	"fmt"
	"io/ioutil"
	"path/filepath"
	"strings"

	"github.com/gin-gonic/gin"
)

type AppStats struct {
	FileParsed bool
	JsonString string
	FileUpload bool
	GistURL    string
}

func main() {
	router := gin.Default()
	apiResponse := AppStats{}
	router.POST("/upload", func(c *gin.Context) {
		formFile, err := c.FormFile("file")
		if err != nil {
			c.JSON(200, gin.H{
				"success": false,
				"payload": "{}",
			})
		}
		// Get raw file bytes - no reader method
		openedFile, _ := formFile.Open()
		file, _ := ioutil.ReadAll(openedFile)
		filename := filepath.Base(formFile.Filename)
		fileExtension := filepath.Ext(filename)
		newFilename := (strings.Split(filename, "."))[0] + ".json"
		JsonString := ""
		fileParsed := false
		fileUpload := false
		fmt.Println(filename)
		fmt.Println(newFilename)
		fmt.Println(file)
		fmt.Println(JsonString)

		if fileExtension == ".yaml" {
			fmt.Println("Its a Yaml file")
		} else if fileExtension == ".csv" {

		} else if fileExtension == ".xlsx" {

		}

		if fileParsed != false && fileUpload != false {

		} else if fileParsed == false {

		} else {
			// file Upload failed
		}

		// Return GIST URL
		c.JSON(200, gin.H{
			"gist_url": apiResponse.GistURL,
		})

	})
	router.Run(":8003")
}
