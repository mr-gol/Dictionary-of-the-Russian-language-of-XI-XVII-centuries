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

function InfoPopup() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");
}
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

function initMultiselect5() {
  checkboxStatusChange5();

  document.addEventListener("click", function(evt) {
    var flyoutElement5 = document.getElementById('myMultiselect5'),
      targetElement5 = evt.target; // clicked element

    do {
      if (targetElement4 == flyoutElement5) {
        // This is a click inside. Do nothing, just return.
        //console.log('click inside');
        return;
      }

      // Go up the DOM
      targetElement4 = targetElement5.parentNode;
    } while (targetElement5);

    // This is a click outside.
    toggleCheckboxArea5(true);
    //console.log('click outside');
  });
}

function checkboxStatusChange5() {
  var multiselect5 = document.getElementById("mySelectLabel5");
  var multiselectOption5 = multiselect5.getElementsByTagName('option')[0];

  var values = [];
  var checkboxes4 = document.getElementById("mySelectOptions5");
  var checkedCheckboxes5 = checkboxes5.querySelectorAll('input[type=checkbox]:checked');

  for (const item of checkedCheckboxes5) {
    var checkboxValue5 = item.getAttribute('value');
    values.push(checkboxValue5);
  }

  var dropdownValue5 = "Nothing is selected";
  if (values.length > 0) {
    dropdownValue5 = values.join(', ');
  }

  multiselectOption5.innerText = dropdownValue5;
}

function toggleCheckboxArea5(onlyHide = false) {
  var checkboxes5 = document.getElementById("mySelectOptions5");
  var displayValue5 = checkboxes5.style.display;

  if (displayValue5 != "block") {
    if (onlyHide == false) {
      checkboxes5.style.display = "block";
    }
  } else {
    checkboxes5.style.display = "none";
  }
}

function initMultiselect6() {
  checkboxStatusChange6();

  document.addEventListener("click", function(evt) {
    var flyoutElement6 = document.getElementById('myMultiselect6'),
      targetElement6 = evt.target; // clicked element

    do {
      if (targetElement6 == flyoutElement6) {
        // This is a click inside. Do nothing, just return.
        //console.log('click inside');
        return;
      }

      // Go up the DOM
      targetElement6 = targetElement6.parentNode;
    } while (targetElement6);

    // This is a click outside.
    toggleCheckboxArea6(true);
    //console.log('click outside');
  });
}

function checkboxStatusChange6() {
  var multiselect6 = document.getElementById("mySelectLabel6");
  var multiselectOption6 = multiselect6.getElementsByTagName('option')[0];

  var values = [];
  var checkboxes6 = document.getElementById("mySelectOptions6");
  var checkedCheckboxes6 = checkboxes6.querySelectorAll('input[type=checkbox]:checked');

  for (const item of checkedCheckboxes6) {
    var checkboxValue6 = item.getAttribute('value');
    values.push(checkboxValue6);
  }

  var dropdownValue6 = "Nothing is selected";
  if (values.length > 0) {
    dropdownValue6 = values.join(', ');
  }

  multiselectOption6.innerText = dropdownValue6;
}

function toggleCheckboxArea6(onlyHide = false) {
  var checkboxes6 = document.getElementById("mySelectOptions6");
  var displayValue6 = checkboxes6.style.display;

  if (displayValue6 != "block") {
    if (onlyHide == false) {
      checkboxes6.style.display = "block";
    }
  } else {
    checkboxes6.style.display = "none";
  }
}

function initMultiselect7() {
  checkboxStatusChange7();

  document.addEventListener("click", function(evt) {
    var flyoutElement7 = document.getElementById('myMultiselect7'),
      targetElement7 = evt.target; // clicked element

    do {
      if (targetElement7 == flyoutElement7) {
        // This is a click inside. Do nothing, just return.
        //console.log('click inside');
        return;
      }

      // Go up the DOM
      targetElement7 = targetElement7.parentNode;
    } while (targetElement7);

    // This is a click outside.
    toggleCheckboxArea7(true);
    //console.log('click outside');
  });
}

function checkboxStatusChange7() {
  var multiselect7 = document.getElementById("mySelectLabel7");
  var multiselectOption7 = multiselect7.getElementsByTagName('option')[0];

  var values = [];
  var checkboxes7 = document.getElementById("mySelectOptions7");
  var checkedCheckboxes7 = checkboxes7.querySelectorAll('input[type=checkbox]:checked');

  for (const item of checkedCheckboxes7) {
    var checkboxValue7 = item.getAttribute('value');
    values.push(checkboxValue7);
  }

  var dropdownValue7 = "Nothing is selected";
  if (values.length > 0) {
    dropdownValue7 = values.join(', ');
  }

  multiselectOption7.innerText = dropdownValue7;
}

function toggleCheckboxArea7(onlyHide = false) {
  var checkboxes7 = document.getElementById("mySelectOptions7");
  var displayValue7 = checkboxes7.style.display;

  if (displayValue7 != "block") {
    if (onlyHide == false) {
      checkboxes7.style.display = "block";
    }
  } else {
    checkboxes7.style.display = "none";
  }
}

function initMultiselect8() {
  checkboxStatusChange8();

  document.addEventListener("click", function(evt) {
    var flyoutElement8 = document.getElementById('myMultiselect8'),
      targetElement8 = evt.target; // clicked element

    do {
      if (targetElement8 == flyoutElement8) {
        // This is a click inside. Do nothing, just return.
        //console.log('click inside');
        return;
      }

      // Go up the DOM
      targetElement8 = targetElement8.parentNode;
    } while (targetElement8);

    // This is a click outside.
    toggleCheckboxArea8(true);
    //console.log('click outside');
  });
}

function checkboxStatusChange8() {
  var multiselect8 = document.getElementById("mySelectLabel8");
  var multiselectOption8 = multiselect8.getElementsByTagName('option')[0];

  var values = [];
  var checkboxes8 = document.getElementById("mySelectOptions8");
  var checkedCheckboxes8 = checkboxes8.querySelectorAll('input[type=checkbox]:checked');

  for (const item of checkedCheckboxes8) {
    var checkboxValue8 = item.getAttribute('value');
    values.push(checkboxValue4);
  }

  var dropdownValue8 = "Nothing is selected";
  if (values.length > 0) {
    dropdownValue8 = values.join(', ');
  }

  multiselectOption8.innerText = dropdownValue8;
}

function toggleCheckboxArea8(onlyHide = false) {
  var checkboxes8 = document.getElementById("mySelectOptions8");
  var displayValue8 = checkboxes4.style.display;

  if (displayValue4 != "block") {
    if (onlyHide == false) {
      checkboxes8.style.display = "block";
    }
  } else {
    checkboxes8.style.display = "none";
  }
}

function initMultiselect9() {
  checkboxStatusChange9();

  document.addEventListener("click", function(evt) {
    var flyoutElement9 = document.getElementById('myMultiselect9'),
      targetElement9 = evt.target; // clicked element

    do {
      if (targetElement9 == flyoutElement9) {
        // This is a click inside. Do nothing, just return.
        //console.log('click inside');
        return;
      }

      // Go up the DOM
      targetElement9 = targetElement9.parentNode;
    } while (targetElement9);

    // This is a click outside.
    toggleCheckboxArea9(true);
    //console.log('click outside');
  });
}

function checkboxStatusChange9() {
  var multiselect9 = document.getElementById("mySelectLabel9");
  var multiselectOption9 = multiselect9.getElementsByTagName('option')[0];

  var values = [];
  var checkboxes9 = document.getElementById("mySelectOptions9");
  var checkedCheckboxes9 = checkboxes9.querySelectorAll('input[type=checkbox]:checked');

  for (const item of checkedCheckboxes9) {
    var checkboxValue9 = item.getAttribute('value');
    values.push(checkboxValue9);
  }

  var dropdownValue9 = "Nothing is selected";
  if (values.length > 0) {
    dropdownValue9 = values.join(', ');
  }

  multiselectOption9.innerText = dropdownValue9;
}

function toggleCheckboxArea9(onlyHide = false) {
  var checkboxes9 = document.getElementById("mySelectOptions9");
  var displayValue9 = checkboxes9.style.display;

  if (displayValue9 != "block") {
    if (onlyHide == false) {
      checkboxes9.style.display = "block";
    }
  } else {
    checkboxes9.style.display = "none";
  }
}

function initMultiselect0() {
  checkboxStatusChange0();

  document.addEventListener("click", function(evt) {
    var flyoutElement0 = document.getElementById('myMultiselect0'),
      targetElement0 = evt.target; // clicked element

    do {
      if (targetElement0 == flyoutElement0) {
        // This is a click inside. Do nothing, just return.
        //console.log('click inside');
        return;
      }

      // Go up the DOM
      targetElement0 = targetElement0.parentNode;
    } while (targetElement0);

    // This is a click outside.
    toggleCheckboxArea0(true);
    //console.log('click outside');
  });
}

function checkboxStatusChange0() {
  var multiselect0 = document.getElementById("mySelectLabel0");
  var multiselectOption0 = multiselect0.getElementsByTagName('option')[0];

  var values = [];
  var checkboxes0 = document.getElementById("mySelectOptions0");
  var checkedCheckboxes0 = checkboxes0.querySelectorAll('input[type=checkbox]:checked');

  for (const item of checkedCheckboxes0) {
    var checkboxValue0 = item.getAttribute('value');
    values.push(checkboxValue0);
  }

  var dropdownValue0 = "Nothing is selected";
  if (values.length > 0) {
    dropdownValue0 = values.join(', ');
  }

  multiselectOption0.innerText = dropdownValue0;
}

function toggleCheckboxArea0(onlyHide = false) {
  var checkboxes0 = document.getElementById("mySelectOptions0");
  var displayValue0 = checkboxes0.style.display;

  if (displayValue0 != "block") {
    if (onlyHide == false) {
      checkboxes0.style.display = "block";
    }
  } else {
    checkboxes0.style.display = "none";
  }
}