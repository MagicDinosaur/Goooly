# Gooly
<div id="top"></div>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Gooly</h3>
  <p align="center">
    A Google-based searching bar
   You can try it on here : http://gooly.phamvietduc.com
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Overview
Gooly is a google-clone search bar with support crawling tool from back-end.  Here is the firstlook:

![gif1](https://user-images.githubusercontent.com/94766118/176983549-dde0d2e9-3f8a-4ba7-9e13-703558f1bcf2.gif)

  
Behind the project is a tool that collects data from public websites and insert to the MySQL database. Here is how it looks:
<p>Terminal</p>
 
![gif2](https://user-images.githubusercontent.com/94766118/176984743-281e9382-dd94-48c3-8a0c-af7fcf12f67f.gif)
<p>Database</p>

![image](https://user-images.githubusercontent.com/94766118/176984831-69761b9a-e69f-47e9-aeff-4b32df683fce.png)

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Django](https://jquery.com)
* [MySQL](https://www.mysql.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Details
### The idea of making this project
  
During my exposure to web programming, I noticed that most websites, especially electronic information sites, adhere to a common standard, in order to increase the number of vistors.  
When inspecting information from these pages, we see the presence of html <meta> tags. These tags will cover the general content of the website such as title, subject image, topic, etc. For example, when I inspect the homepage of Cnet and The Verge, we could se that there are some similiar in naming html tags such as "og:site_name", "og:description",,...
*Inspecting Cnet*
![image](https://user-images.githubusercontent.com/94766118/176985569-f4a83361-2027-4f8e-a1b4-5631a7fee139.png)
*Inspecting the verge*
![image](https://user-images.githubusercontent.com/94766118/176985604-7125a04a-5594-49f4-a403-c70b87fbba0b.png)

With that ideas in mind, I started developing a tool that could recursively call in the meta tags and anchor tags of public websites, and collect the data into the database. The collected data is served to search engines.



### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/MagicDinosaur/Goooly.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#top">back to top</a>)</p>






<!-- ROADMAP -->
## Roadmap
There are some exciting challenges that I could add into my project in the near future.  

- [x] Add searching Image and voice
- [ ] Redesign database for better searching 
- [ ] Implement Natural Language Processing ML models (GPT, BERT, Transformer) to enhance the quality of search queries
- [ ] Optimize crawling engine (first try with asynchronous I/O)
- [x] Multi-language Support
    - [ ] Vietnamese
    - [ ] English


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion or feature idea that would make this better, please fork the repo and create a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Duc Pham -  - phamvduc2112@gmail.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>




