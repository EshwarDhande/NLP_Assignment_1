# NLP_Assignment_1

ASSIGNED LANGUAGE - **MARATHI**
---

<center style="font-size:18px"><b><u>Task 1. Curating Dataset</b></u></center>

  <h4><i>a. Crawling</h4></i>

- Most of the crawling part was done on about 45 news websites
- Other sources for crawling include Marathi Wikipedia, Shabdkosh, etc 
- Some websites consisted of images for which OCR data extraction was used 

<h4><i>b. Downloading data from existing corpora</h4></i>

- We found several sources with well-curated Marathi data, details of which are in the next section.
- Data were downloaded from sources like Kaggle, Github, etc.




<center style="font-size:18px"><b><u>Task 2. Statistics</b></u></center>

<br>
<b><i><h3>I. Downloaded data:</h3></b></i>
<table>
  <tr>
    <th style="font-size:16px">Dataset Source name</th>
    <th style="font-size:16px">Volume in GB</th>
    <th style="font-size:16px">Total number of articles</th>
  </tr>
  <tr>
    <td style="font-size:16px">Oscar Marathi</td>
    <td style="font-size:16px">4.2</td>
    <td style="font-size:16px">729578</td>
  </tr>
  <tr>
    <td style="font-size:16px">Samanantar</td>
    <td style="font-size:16px">0.61</td>
    <td style="font-size:16px">Row 2 Col3</td>
  </tr>
  <tr>
    <td style="font-size:16px">Sangrah</td>
    <td style="font-size:16px">30</td>
    <td style="font-size:16px">177265460</td>
  </tr>
  <tr>
    <td style="font-size:16px">MNATD</td>
    <td style="font-size:16px">5</td>
    <td style="font-size:16px">Row 2 Col3</td>
  </tr>
  <tr>
    <td style="font-size:16px">CulturaX</td>
    <td style="font-size:16px">16.93</td>
    <td style="font-size:16px">Row 2 Col3</td>
  </tr>
  <tr>
    <td style="font-size:16px">MADLAD-400</td>
    <td style="font-size:16px">21</td>
    <td style="font-size:16px">Row 2 Col3</td>
  </tr>
  <tr>
    <td style="font-size:16px">Glot500-c</td>
    <td style="font-size:16px">9.2</td>
    <td style="font-size:16px">Row 2 Col3</td>
  </tr>

</table>


<br>
<b><i><h3>II. Crawled data:</h3></b></i>
  
| Sr. No. | Source                            | No. of Articles | Size    |
|---------|------------------------------------|-----------------|---------|
| 1       | Beed Reporter                      | 822             | 3.35 MB |
| 2       | Dainik Prabhat                     | 89630           | 1.3 GB  |
| 3       | Deshdoot                           | 33099           | 317 MB  |
| 4       | Deshonnati                         | 245             | 3.44 MB |
| 5       | Divya Marathi                      | 1235            | 743 KB  |
| 6       | Ekmat                              | 7012            | 29.4 MB |
| 7       | Gavkari                            | 2387            | 99.4 MB |
| 8       | Goenkar                            | 227             | 4.5 MB  |
| 9       | Janta Awaaj                        | 3371            | 49 MB   |
| 10      | Lokmat                             | 1398            | 21 MB   |
| 11      | Loksatta                           | 784             | 20 MB   |
| 12      | Maharashtra Times                  | 342719          | 5.6 GB  |
| 13      | Mahasatta                          | 1683            | 17 MB   |
| 14      | Mumbai Tarun Bharat                | 102             | 788 KB  |
| 15      | Nava Kaal                          | 4               | 5.5 MB  |
| 16      | Nava Maratha                       | 3499            | 39 MB   |
| 17      | matrubharti                        | 10016           | 172 MB  |
| 18      | Prabhudha Bharat                   | 2010            | 22 MB   |
| 19      | Prahaar                            | 25967           | 526 MB  |
| 20      | Pratahkal                          | 503             | 3.1 MB  |
| 21      | Pudhari (freepress journal)        | 51              | 400 KB  |
| 22      | Rashtra Sanchar                    | 4413            | 89.4 MB |
| 23      | Rashtramat                         | 9854            | 71 MB   |
| 24      | Saamana                            | 22352           | 146 MB  |
| 25      | Sakaal                             | 1.05            | 9.37 GB |
| 26      | Tarun Bharat                       | 11897           | 173 MB  |
| 27      | Sanatan Prabhat                    | 94227           | 413 MB  |
| 28      | Inmarathi                          | 29619           | 268 MB  |
| 29      | Jai Maharashtra (dy)               | 80              | 344 KB  |
| 30      | Lokshahi                           | 44868           | 292 MB  |
| 31      | NDTV Marathi                       | 82409           | 353 MB  |
| 32      | Marathi ABP                       | 6872            | 110 MB  |
| 33      | Saam TV                            | 12457           | 88 MB   |
| 34      | TV9 Marathi                        | 1816            | 16 MB   |
| 35      | ZEE 24 Taas                        | 144595          | 1.5 GB  |
| 36      | Divya Marathi (dainik bhaskar)     | 84              | 840 KB  |


<center> <b> <h3> Total data collected - xyz + abc = 150GB</b></h3></center>




<center style="font-size:18px"><b><u>Task 3 </b></u></center>  
  

  
- While crawling the data, we made sure each article was added as a new article  


---


<center style="font-size:18px"><b><u>Task 4: List of bad bad-word dictionaries for Marathi</b></u></center>
<br>
- We could find most of the bad words in an already curated repository. https://github.com/Adi2K/MarathiSwear/blob/master/profane.txt


---


<center style="font-size:18px"><b><u>Task 5: Data Cleaning</b></u></center>


- We removed any other script apart from Devnagari.
- We removed bad words using regex and pandas.
- The cleaning script can be found here.

---


<center style="font-size:18px"><b><u>Task 6: Statistics</b></u></center>

<table>
  <tr>
    <th style="font-size:18px">Before Cleaning</th>
    <th style="font-size:18px">After Cleaning </th>
    
  </tr>
  <tr>
    <td style="font-size:16px">Row 1 Col1</td>
    <td style="font-size:16px">Row 1 Col2</td>
    
  </tr>
  <tr>
    <td style="font-size:16px">Row 2 Col1</td>
    <td style="font-size:16px">Row 2 Col2</td>
    
  </tr>
</table>



---
<center style="font-size:18px"><b><u>Task 7: Deduplication</u></b></center>  
<br>

- The script for deduplication can be found here. 
- We have utilized min hash and jaccard similarity to find if two documents are similar using threshold value of 0.2


---
<center style="font-size:18px"><b><u>Task 8: Statistics</u></b></center>
<br>

<table>
  <tr>
    <th></th>
    <th style="font-size:16px">Before Deduplication</th>
    <th style="font-size:16px">After Deduplication </th>
    
  </tr>
  <tr>
    <td style="font-size:16px"><b>Total Articles</b></td>
    <td style="font-size:16px">Row 1 Col1</td>
    <td style="font-size:16px">Row 1 Col2</td>
    
  </tr>
  <tr>
  <td style="font-size:16px"> <b>Total Size</b></td>
    <td style="font-size:16px">Row 2 Col1</td>
    <td style="font-size:16px">Row 2 Col2</td>
    
  </tr>
</table>


---

## ***Individual Contribution***




|       Team member     | Contribution|
|       ------------    |------------|
| `Mukul Paras Potta` | Wrote code for crawling, crawled news websites, Wrote code for deduplication, Crawled 9 news websites|
| `Manish Bairwa`  | Collection of Rajasthani(language assigned earlier) Data sources and scraping, Crawled 9 news websites |
| `Isha Narang`  | Wrote code for curating data from pdf sources using OCR, Crawled 9 news websites, and Created this report. |
| `Eshwar Dhande`   | Collection of source and public datasets, Collected 45 news website sources, Verifying and adding to the list of bad words, Crawled 9 news websites|
| `Preyum Kumar ` |Crawled 9 news websites, some of which contained PDFs and images which were retrieved using OCR |


<h4><i>Note - The earlier assigned language was Rajasthani, for which everyone equally contributed to scraping the data from collected websites.</h4></i>
---

