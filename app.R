library(shiny)
library(shinydashboard)
library(shinyjs)
library(shinyFiles)
## Load in Data Structure
df = read.table("data/merged_frames.RData")

## Java Script to allow user to hit Enter
jscode <- '
$(function() {
  var $els = $("[data-proxy-click]");
  $.each(
    $els,
    function(idx, el) {
      var $el = $(el);
      var $proxy = $("#" + $el.data("proxyClick"));
      $el.keydown(function (e) {
        if (e.keyCode == 13) {
          $proxy.click();
        }
      });
    }
  );
});
'

ui = dashboardPage(
  dashboardHeader(title = "GRAB"),
  dashboardSidebar(checkboxGroupInput("assembly", label = h3("Assembly Level"), 
                                  choices = list("Complete Genomes" = "Complete Genome", "Scaffolds" = "Scaffold", "Chromosomes" = "Chromosome", "Contigs" = "Contig"),
                                  selected = "Complete Genome"),hr(),fluidRow(column(3, verbatimTextOutput("value")),
               selectInput("taxonomy", "Select Taxonomic Level", choices = c("Phylum", "Class", "Order", "Family", "Genus", "Species", "Subspecies")),
               selectInput("material", "Select Type of Genetic Information", choices = c("Genome", "Coding", "Protein"))
               )),
  dashboardBody(
    useShinyjs(),
    h4("Press Go! to view table filtered by taxonomic query"),
    actionButton("goButton", "Go!"),
    
    tags$head(tags$script(HTML(jscode))),
    h3("Input Organismal Query"),
    h4("Please input organismal names seperated by either commas or spaces"),
    tagAppendAttributes(textInput("query", label = "", value = ""), `data-proxy-click` = "goButton"),
    
    ## Hide certain buttons to prevent out of order
    hidden(
    actionButton("down", "Download Sequences to Server"),
    downloadButton("downloadData", "Download Sequences to Local"),
    tableOutput("tabs")
    )
  
  
))

server = function(input, output, session) {

    values = reactiveValues(df_data = NULL)

    observeEvent(input$goButton, {
      tax = tolower(input$taxonomy)
      ref = input$assembly
      query = tolower(input$query)
      
      ## Split Query
      my_list = strsplit(query, split = c(" ", ","))
      
      ## Filter data table by Query
      matches <- df[grep(paste(my_list,collapse="|"),df[,tax], ignore.case = T),]
      
      ## filter by checkbox level
      values$df_data <- matches[grep(paste(ref,collapse="|"),matches[,"assembly_level"], ignore.case = T),]
      
      show("down")
      show("tabs")
    })
  
    
    
    output$tabs <- renderTable({values$df_data})
    
    observeEvent(input$down, {
      mat = input$material
      print(input$query)
      temp = values$df_data
      
      calls = as.character(temp$ftp_path)
      
      call_base = basename(calls)
      test = paste(calls,call_base, sep = '/')
      
      
      if(mat == 'Protein'){
        temp = paste(test, "protein.faa.gz'",sep = "_")
        wpath = paste("wget ", temp, sep = "'")
      } else if(mat == 'Coding'){
        temp = paste(test, "cds_from_genomic.fna.gz'", sep = "_")
        wpath = paste("wget ", temp, sep = "'")
      } else{
        temp = paste(test, "genomic.fna.gz'", sep = "_")
        wpath = paste("wget ", temp, sep = "'")
      }
      
      if (file.exists("/srv/connect/apps/GRAB/GRAB_Sequences")){
        system("rm -r -f /srv/connect/apps/GRAB/GRAB_Sequences")
        system("mkdir /srv/connect/apps/GRAB/GRAB_Sequences")
      } else {
        system("mkdir /srv/connect/apps/GRAB/GRAB_Sequences")
      }
      
      setwd("./GRAB_Sequences")
      lapply(wpath, system)
      setwd("..")
      if (file.exists("/srv/connect/apps/GRAB/GRAB_Sequences.zip")){
        system("rm -r -f /srv/connect/apps/GRAB/GRAB_Sequences.zip")
        system("zip -r GRAB_Sequences.zip GRAB_Sequences")
      } else{
        system("zip -r GRAB_Sequences.zip GRAB_Sequences")
      }
      
      show('downloadData')
      
    })
    
    output$downloadData <- downloadHandler(
      filename <- function() {
        paste("GRAB_Download", "zip", sep=".")
      },
      
      content <- function(file) {
        file.copy("/srv/connect/apps/GRAB/GRAB_Sequences.zip", file)
      },
      contentType = "application/zip"
    )
    
    ## Adding File System
    
}

shinyApp(ui = ui, server = server)



