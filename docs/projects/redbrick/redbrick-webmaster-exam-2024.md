# Redbrick Webmaster Exam: AGM 2024 - cheese

*[GitHub Repository Link](https://github.com/CheeseLad/redbrick-webmaster-exam-2024)*

|                |                  |
| -------------- | ---------------- |
| Time allocated | 24 hours         |
| Start          | 16:00 20/03/2024 |
| End            | 16:00 21/03/2024 |

> [!NOTE] This exam consists of 2 sections: theory and practical. You must score 60% in each section; overall mark does not matter.

> [!WARNING] This exam is open book, but do not blindly follow online resources. Evidence of copy and pasting or generative AI will be apparent in the practical section. Concise, coherent and accurate answers will be marked favourably in the theory section.

## Theory Section

1. State a method of horizontally centering a  `<div>` HTML element with CSS.

```
Add margin: auto; and width: 50%; to the div element's CSS.
```

2. What is the key difference between the `<div>` and `<span>` HTML elements?

```
A div element is used for block-level organization and styling of page elements, whereas a span element is used for inline organization and styling.
```

3. Explain the `srcset` and `sizes` HTML attributes and their role in implementing responsive images on the web.

```
The srcset attribute allows you to specify multiple image sources along with their respective descriptors. 

The sizes attribute informs the browser about the intended display size of the image under different conditions (e.g., viewport size, screen resolution)
```

4. What do the terms SEO and ARIA mean, in relation to the web? What are the semantic HTML elements, and how do they relate to SEO and ARIA?

```
SEO: Search Engine Optimisation. SEO means the process of improving your website to increase its visibility in Google, Microsoft Bing, Yahoo, and other search engines.

ARIA: Accessible Rich Internet Applications. It consists of markup that can be added to HTML in order to communicate the roles, states, and properties of user interface elements to assistive technologies.

Semantic HTML elements help you create a clear and logical layout for your web pages, making them easier to be understood by screen readers for ARIA and search engines for SEO.
```

5. What are events in JavaScript, and how does event bubbling work? How is event bubbling utilised in event delegation?

```
An event is an action that occurs as per the user's instruction as input and gives the output in response. Examples include clicking a button, hovering over an element, or submitting a form.

Event bubbling happens when an element receives an event, and that event is transmitted to its parent and ancestor elements in the DOM tree until it gets to the root element.
```

6. What are Web Components? Briefly describe the *three* main technologies which compose the Web Component specification.

```
Web components are a set of web platform APIs that allow you to create new custom, reusable, encapsulated HTML tags to use in web pages and web apps.
```

7. List the *four* CRUD operations and the respective HTTP method for each.

```
Create - POST
Read - GET
Update - PUT
Delete - DELETE
```

8. What does REST stand for, and what are the key principles of a RESTful API?

```
REST stands for Representational State Transfer.

Key Principles:

Uniform Interface
Stateless
Cacheable
Client-Server Design Pattern
Layered System
```

9. Explain the `Authorization` HTTP header and *two* valid schemes that can be used.

```
The HTTP Authorization request header can be used to provide credentials that authenticate a user agent with a server, allowing access to a protected resource.

Bearer Token: Allows a client to authenticate using a token.
Basic Authentication: Allows a client to authenticate using a username and password.
```

10. Describe HTTPS (HTTP Secure) communication and the main advantage over HTTP.

```
HTTPS is HTTP with encryption and verification. 

The main advantage is HTTPS uses TLS (SSL) to encrypt normal HTTP requests and responses, and to digitally sign those requests and responses. As a result, HTTPS is far more secure than HTTP.
```

11. How does browser caching work, and why is it important?

```
Caching is the process of storing copies of files in a cache, or temporary storage location, so that they can be accessed more quickly.

To shorten page load times, browsers cache most of the content that appears on the webpage, saving a copy of the webpage's content on the device’s hard drive.
```

12. What is the main purpose of a Content Delivery Network (CDN)?

```
A content delivery network (CDN) is a geographically distributed group of servers that caches content close to end users. A CDN allows for the quick transfer of assets needed for loading Internet content, including HTML pages, JavaScript files, stylesheets, images, and videos. 
```

13. Briefly describe the processes of file minification, bundling, and compression, in the context of web performance.

```
Minification involves removing unnecessary characters from source code without affecting its functionality. This includes removing whitespace, comments, and shortening variable names.

Bundling involves combining multiple files of the same type into a single file. For example, instead of loading several separate CSS or JavaScript files, bundling consolidates them into one.

Compression reduces the size of files by encoding them in a more efficient format before they are sent over the network.
```

14. What is a bundler in web development? List *two* popular bundlers used in modern projects.

```
A bundler is a development tool that combines many JavaScript code files into a single one that is production-ready loadable in the browser. A bundler's operation is divided into two stages: dependency graph generation and eventual bundling.

Parcel is a plug-and-play, zero-configuration build tool that allows developers to configure multi-assets quickly (e.g., JS, CSS, and HTML) modules necessary for development.

Browserify is an open-source Javascript bundler that allows you to bundle Node.js files that the browser can run. With Browserify, developers can use node-style require() to load npm modules in the browser. 
```

15. Compare and contrast Single Page Applications (SPAs) and Multi-Page Applications (MPAs), including their definitions, key characteristics, and use-cases.

```
Single Page Applications (SPAs) are web applications that load a single HTML page and dynamically update that page as the user interacts with it, typically using JavaScript frameworks like React or Angular. They offer a seamless, app-like experience with faster transitions between pages. Multi-Page Applications (MPAs), on the other hand, consist of multiple HTML pages, each serving distinct content. While MPAs are simpler to develop and maintain, SPAs are more suitable for complex, interactive web applications requiring real-time updates and smooth transitions between views.
```

16. Describe the Jamstack software architecture, its benefits, and its main differences from traditional server-driven architectures.

```
Jamstack, an acronym for JavaScript, APIs, and Markup, represents a modern web development architecture that offers numerous benefits over traditional monolithic setups. At its core, Jamstack decouples the frontend presentation layer from the backend logic, resulting in a more efficient and agile development process.
```

17. What is a Static Site Generator (SSG)? List *two* popular SSGs in the Jamstack ecosystem and give reasons for their popularity.

```
Static site generators are engines that use text input files (such as Markdown and AsciiDoc) to generate static web pages, producing relevant HTML, CSS, and JavaScript.

Two Popular SSGs:

Hugo: Written in Go and is known for its speed and flexibility.

11ty: Allows developers to use various templating languages and data formats to generate static websites.
```

18. How is data integrated in Jamstack web applications, during both run-time and build-time, from data sources such as Content Management Systems (CMS) and third-party APIs?

```
During build-time, data is fetched from sources like Content Management Systems and third-party APIs and pre-rendered into static assets. This approach optimizes performance by reducing server load and ensuring faster page loads for users. Additionally, run-time integration enables dynamic content updates and interactions through client-side JavaScript fetching data from APIs as needed.
```

19. What is Server-Side Rendering (SSR) and Hydration, and when would they be used in Jamstack web applications?

```
Server-side rendering (SSR) is when an application serves plain HTML to the client. SSR can be divided into two types: SSR with hydration and SSR without hydration. SSR is an old technique used by older frameworks such as WordPress, Ruby on Rails, and ASP.NET.

Newer solutions like Next.js uses hydration, where the static HTML will be hydrated on the client side using JavaScript. Think of it like instant coffee, the coffee powder is the HTML, and the water is the JavaScript. What happens when you mix instant coffee powder with water? You get — wait for it — coffee.
```

20. Briefly describe serverless functions and their role in implementing dynamic functionality in Jamstack web applications at run-time.

```
Serverless functions augment the Jamstack approach to web application development by providing a way to develop and deploy CRUD functionality without relying as heavily on third-party APIs to handle and process the application's requests.
```

## Practical Section

```
Instructions

pip install -r requirements.txt
cd site
npm install -g vite
npm install vite --save-dev

Order Frontend Site: http://127.0.0.1:8000/
API Hoodie List: http://127.0.0.1:8001/api/hoodie/
Single Hoodie: http://127.0.0.1:8001/api/hoodie/1/
Order Hoodie Post Area: http://127.0.0.1:8001/hoodies/
Static Files Example: http://127.0.0.1:8002/staticfiles/img/blue.png
```

>[!INFO] This practical is technology-agnostic, so you have freedom to choose frameworks and the tech stack. This will assess not only your expertise with web technologies but also your choice of software architecture for the requirements. An excellent practical satisfies the steps below, while going beyond what is required to create a simple project with solid UI, maintainability, security and performance.

### 1. Set Up Git Repository

- Create a Git repository on GitHub.
- Give `@JedHazaymeh` admin access to the repository.

### 2. Set Up Project Structure

- Create a directory called `site`.
- Work within the `site` directory for the frontend development.

### 3. Create Hoodie Purchase Form

- Create a simple HTML form with the following input fields:
    - Username
    - Affiliation (Redbrick/Blueblock)
    - Size (XS/S/M/L/XL)
    - Amount
- Apply styling to the fields:
    - Drop shadows
    - Rounded corners
    - Border colour change on focus with a transition
- Add an image above the form displaying a hoodie based on the `Affiliation` field.
- Validate the following fields on form submission:
    - Username:
        - Input is 4-16 characters in length.
        - Contains only alphanumeric characters, -, _.
    - Amount:
        - Input is a number.
        - Input is within the range 1-5.

### 4. Set Up Development Server

- Include a simple dev server to locally serve the static files.
- You can use Vite, a bundler, or a static site generator for this purpose.

### 5. Set Up API Service

- In the root directory, create a directory called `api`.
- Work within the `api` directory for the backend development.
- Create a simple RESTful API service using a HTTP request multiplexer (mux) written with Express.js, FastAPI, etc.
- Add a `POST /hoodies` endpoint to accept the form data and respond with a rendered HTML page containing the order confirmation.

### 6. Connect Frontend with Backend

- Edit the form in the `site` directory to send the HTTP request to the API and render the page response accordingly.

### 7. Update & Secure on GitHubv

- Push all the changes to the GitHub repository.
- On GitHub, secure the main branch so that no more changes can be pushed without a pull request.
