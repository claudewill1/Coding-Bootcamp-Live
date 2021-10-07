const testNode = document.getElementById("test");

function btnEvent(id, action) {
  document.getElementById(`${id}`).addEventListener("click", () => {
    switch(action){
      case 1:
        testNode.innerHTML = +testNode.innerHTML - 1;
        break;
      case 2:
        testNode.innerHTML = +testNode.innerHTML + 1;
        break;   
    }
  });
}
                                                    
btnEvent("btn", 1);
btnEvent("btn2", 2);