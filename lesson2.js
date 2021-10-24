function myFunc(){
    let i = 1;
    let tag = document.getElementById("pleasechange");
    for(i = 1; i <= 100; ++i) {
        if((i % 3 == 0) && (i % 5 != 0)) {
            tag.innerHTML = "Fizz";
        }
        else if ((i % 5 == 0) && (i % 3 != 0)) {
            tag.innerHTML = "Buzz";
        }
        else if((i % 3 == 0) && (i % 5 == 0)) {
            tag.innerhtml = "FizzBuzz";
        }
        else {
            tag.innerhtml = i;
        }
    }
    

    // Change CSS style
    let hTags = document.getElementsByClassName("heading");
    for(let i = 0; i < hTags.length; ++i) {
        hTags[i].style.color = "yellow";
    }
}

myFunc();
