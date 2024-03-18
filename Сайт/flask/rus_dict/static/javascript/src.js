window.onload = (event) => {
  initMultiselect();
};

window.onload = (event) => {
  initMultiselect2();
};

window.onload = (event) => {
  initMultiselect3();
};

window.onload = (event) => {
  initMultiselect4();
};


function initMultiselect() {
  checkboxStatusChange();

  document.addEventListener("click", function(evt) {
    var flyoutElement = document.getElementById('myMultiselect'),
      targetElement = evt.target; // clicked element

    do {
      if (targetElement == flyoutElement) {
        // This is a click inside. Do nothing, just return.
        //console.log('click inside');
        return;
      }

      // Go up the DOM
      targetElement = targetElement.parentNode;
    } while (targetElement);

    // This is a click outside.
    toggleCheckboxArea(true);
    //console.log('click outside');
  });
}

function checkboxStatusChange() {
  var multiselect = document.getElementById("mySelectLabel");
  var multiselectOption = multiselect.getElementsByTagName('option')[0];

  var values = [];
  var checkboxes = document.getElementById("mySelectOptions");
  var checkedCheckboxes = checkboxes.querySelectorAll('input[type=checkbox]:checked');

  for (const item of checkedCheckboxes) {
    var checkboxValue = item.getAttribute('value');
    values.push(checkboxValue);
  }

  var dropdownValue = "Nothing is selected";
  if (values.length > 0) {
    dropdownValue = values.join(', ');
  }

  multiselectOption.innerText = dropdownValue;
}

function toggleCheckboxArea(onlyHide = false) {
  var checkboxes = document.getElementById("mySelectOptions");
  var displayValue = checkboxes.style.display;

  if (displayValue != "block") {
    if (onlyHide == false) {
      checkboxes.style.display = "block";
    }
  } else {
    checkboxes.style.display = "none";
  }
}

function initMultiselect2() {
  checkboxStatusChange2();

  document.addEventListener("click", function(evt) {
    var flyoutElement2 = document.getElementById('myMultiselect2'),
      targetElement2 = evt.target; // clicked element

    do {
      if (targetElement2 == flyoutElement2) {
        // This is a click inside. Do nothing, just return.
        //console.log('click inside');
        return;
      }

      // Go up the DOM
      targetElement2 = targetElement2.parentNode;
    } while (targetElement2);

    // This is a click outside.
    toggleCheckboxArea2(true);
    //console.log('click outside');
  });
}

function checkboxStatusChange2() {
  var multiselect2 = document.getElementById("mySelectLabel2");
  var multiselectOption2 = multiselect2.getElementsByTagName('option')[0];

  var values = [];
  var checkboxes2 = document.getElementById("mySelectOptions2");
  var checkedCheckboxes2 = checkboxes2.querySelectorAll('input[type=checkbox]:checked');

  for (const item of checkedCheckboxes2) {
    var checkboxValue2 = item.getAttribute('value');
    values.push(checkboxValue2);
  }

  var dropdownValue2 = "Nothing is selected";
  if (values.length > 0) {
    dropdownValue2 = values.join(', ');
  }

  multiselectOption2.innerText = dropdownValue2;
}

function toggleCheckboxArea2(onlyHide = false) {
  var checkboxes2 = document.getElementById("mySelectOptions2");
  var displayValue2 = checkboxes2.style.display;

  if (displayValue2 != "block") {
    if (onlyHide == false) {
      checkboxes2.style.display = "block";
    }
  } else {
    checkboxes2.style.display = "none";
  }
}

function initMultiselect3() {
  checkboxStatusChange3();

  document.addEventListener("click", function(evt) {
    var flyoutElement3 = document.getElementById('myMultiselect3'),
      targetElement3 = evt.target; // clicked element

    do {
      if (targetElement3 == flyoutElement3) {
        // This is a click inside. Do nothing, just return.
        //console.log('click inside');
        return;
      }

      // Go up the DOM
      targetElement3 = targetElement3.parentNode;
    } while (targetElement3);

    // This is a click outside.
    toggleCheckboxArea3(true);
    //console.log('click outside');
  });
}

function checkboxStatusChange3() {
  var multiselect3 = document.getElementById("mySelectLabel3");
  var multiselectOption3 = multiselect3.getElementsByTagName('option')[0];

  var values = [];
  var checkboxes3 = document.getElementById("mySelectOptions3");
  var checkedCheckboxes3 = checkboxes3.querySelectorAll('input[type=checkbox]:checked');

  for (const item of checkedCheckboxes3) {
    var checkboxValue3 = item.getAttribute('value');
    values.push(checkboxValue3);
  }

  var dropdownValue3 = "Nothing is selected";
  if (values.length > 0) {
    dropdownValue3 = values.join(', ');
  }

  multiselectOption3.innerText = dropdownValue3;
}

function toggleCheckboxArea3(onlyHide = false) {
  var checkboxes3 = document.getElementById("mySelectOptions3");
  var displayValue3 = checkboxes3.style.display;

  if (displayValue3 != "block") {
    if (onlyHide == false) {
      checkboxes3.style.display = "block";
    }
  } else {
    checkboxes3.style.display = "none";
  }
}

function initMultiselect4() {
  checkboxStatusChange4();

  document.addEventListener("click", function(evt) {
    var flyoutElement4 = document.getElementById('myMultiselect4'),
      targetElement4 = evt.target; // clicked element

    do {
      if (targetElement4 == flyoutElement4) {
        // This is a click inside. Do nothing, just return.
        //console.log('click inside');
        return;
      }

      // Go up the DOM
      targetElement4 = targetElement4.parentNode;
    } while (targetElement4);

    // This is a click outside.
    toggleCheckboxArea4(true);
    //console.log('click outside');
  });
}

function checkboxStatusChange4() {
  var multiselect4 = document.getElementById("mySelectLabel4");
  var multiselectOption4 = multiselect4.getElementsByTagName('option')[0];

  var values = [];
  var checkboxes4 = document.getElementById("mySelectOptions4");
  var checkedCheckboxes4 = checkboxes4.querySelectorAll('input[type=checkbox]:checked');

  for (const item of checkedCheckboxes4) {
    var checkboxValue4 = item.getAttribute('value');
    values.push(checkboxValue4);
  }

  var dropdownValue4 = "Nothing is selected";
  if (values.length > 0) {
    dropdownValue4 = values.join(', ');
  }

  multiselectOption4.innerText = dropdownValue4;
}

function toggleCheckboxArea4(onlyHide = false) {
    var checkboxes4 = document.getElementById("mySelectOptions4");
    var displayValue4 = checkboxes4.style.display;

    if (displayValue4 != "block") {
        if (onlyHide == false) {
            checkboxes4.style.display = "block";
        }
    } else {
        checkboxes4.style.display = "none";
    }
}