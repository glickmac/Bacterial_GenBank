library(shiny)
library(shinydashboard)
library(shinyjs)
library(ggplot2)

## Load in Phyloseq Structure
df = read.table("data/merged_frames.RData")



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
                                  selected = "Complete Genomes"),hr(),fluidRow(column(3, verbatimTextOutput("value")),
               selectInput("taxonomy", "Select Taxonomic Level", choices = c("Phylum", "Class", "Order", "Family", "Genus", "Species", "Subspecies"))
               )),
  dashboardBody(
    useShinyjs(),
    actionButton("goButton", "Go!"),
    tags$head(tags$script(HTML(jscode))),
    tagAppendAttributes(textInput("query", label = h3("Input Organismal Query"), value = ""), `data-proxy-click` = "goButton"),
    h4("Please input organismal names seperated by either commas or spaces"),
    downloadButton("downloadData", "Download")
    )
)

server = function(input, output, session) {
  observeEvent(input$goButton, {
    cat(input$query, "\n")
  })
  #x = strsplit(input$query, split = ",")
  
  
  # Downloadable csv of selected dataset ----
  #output$downloadData <- "Hello World"
}

shinyApp(ui = ui, server = server)



