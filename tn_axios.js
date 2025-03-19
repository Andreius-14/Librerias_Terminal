import axios from "axios";
// ____            _
//| __ )  __ _ ___(_) ___ ___
//|  _ \ / _` / __| |/ __/ _ \
//| |_) | (_| \__ \ | (_| (_) |
//|____/ \__,_|___/_|\___\___/
//

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 GET                   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/
//axios
//  .get("https://jsonplaceholder.typicode.com/comments")
//  .then((res) => {
//    console.log(res.data);
//  })
//  .catch((err) => {
//    console.error(err);
//  });

// GET - Multiple
//axios
//  .all([
//    axios.get("https://jsonplaceholder.typicode.com/comments?_limit=2"),
//    axios.get("https://jsonplaceholder.typicode.com/posts?_limit=2"),
//  ])
//  .then(
//    axios.spread((comments, posts) => {
//      console.log(comments.data);
//      console.log(posts.data);
//    }),
//  )
//  .catch((err) => console.error(err));

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 POST                  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/
//axios
//  .post("https://jsonplaceholder.typicode.com/comments", {
//    name: "Jackson Smith",
//    email: "jsmith@example.com",
//    body: "This is a piece of art.",
//  })
//  .then((res) => {
//    console.log(res.data);
//  })
//  .catch((err) => {
//    console.error(err);
//  });

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          UPDATE (PUT/PATCH)           ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/

// Before
axios
  .get("https://jsonplaceholder.typicode.com/comments/100")
  .then((res) => {
    console.log(res.data.email);
  })
  .catch((err) => {
    console.error(err);
  });

// After
axios
  .patch("https://jsonplaceholder.typicode.com/comments/100", {
    email: "donaymilin@ether.com",
  })
  .then((res) => {
    console.log(res.data.email);
  })
  .catch((err) => {
    console.error(err);
  });

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                DELETE                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/
axios
  .delete("https://jsonplaceholder.typicode.com/comments/10")
  .then((res) => {
    console.log(res.data);
  })
  .catch((err) => {
    console.error(err);
  });

//    _                                _
//   / \__   ____ _ _ __  ______ _  __| | ___
//  / _ \ \ / / _` | '_ \|_  / _` |/ _` |/ _ \
// / ___ \ V / (_| | | | |/ / (_| | (_| | (_) |
///_/   \_\_/ \__,_|_| |_/___\__,_|\__,_|\___/
//

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃            CONFIGURACION              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/
axios({
  method: "get",
  url: "https://jsonplaceholder.typicode.com/posts/1",
  timeout: 5000, // 5 segundos
  headers: { Authorization: "Bearer token123" },
})
  .then((response) => console.log(response.data))
  .catch((error) => console.error("Error:", error));

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                  ALL                  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/

// llamadas Multiple
axios
  .all([
    axios.get("https://jsonplaceholder.typicode.com/posts/1"),
    axios.get("https://jsonplaceholder.typicode.com/posts/2"),
  ])
  .then(
    axios.spread((post1, post2) => {
      console.log("Post 1:", post1.data);
      console.log("Post 2:", post2.data);
    }),
  )
  .catch((error) => console.error("Error:", error));

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃            ASYNC Y AWAIT              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/

async function obtenerDatos() {
  try {
    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/posts/1",
    );
    console.log("Datos:", response.data);
  } catch (error) {
    console.error("Error:", error);
  }
}

obtenerDatos();

/*
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃              INSTANCIA                ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
*/

const api = axios.create({
  baseURL: "https://jsonplaceholder.typicode.com",
  timeout: 5000,
  headers: { "Content-Type": "application/json" },
});

api
  .get("/posts/1")
  .then((response) => console.log(response.data))
  .catch((error) => console.error("Error:", error));
