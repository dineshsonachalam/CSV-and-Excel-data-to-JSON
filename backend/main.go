package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"path/filepath"

	"github.com/gin-gonic/gin"
	"sigs.k8s.io/yaml"
)

type ApiResponse struct {
	success bool
	payload string
	message string
}

// func YamlToJSON(data []byte) ApiResponse {

// }

func main() {
	router := gin.Default()
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
		// fmt.Println(file)
		var results ApiResponse
		if fileExtension == ".yaml" || fileExtension == ".yml" {
			parsedData, _ := yaml.YAMLToJSON(file)
			fmt.Println(string(parsedData))
			c.JSON(200, gin.H{
				"success": "f",
				"payload": bytes.NewBuffer(parsedData),
			})
		}

		// } else if fileExtension == ".csv" {

		// } else if fileExtension == ".xlsx" {

		// } else if fileExtension == ".xls" {

		// } else {

		// }
		fmt.Println("Payload: ", results.payload)

		// c.JSON(200, gin.H{
		// 	"success": "f",
		// 	"payload": "fdf",
		// })

	})
	router.Run(":8003")
}

// Reference: https://stackoverflow.com/questions/39037049/how-to-upload-a-file-and-json-data-in-postman
// https://i.imgur.com/J2v6Tf0.png
