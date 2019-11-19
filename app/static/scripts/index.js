document.addEventListener('DOMContentLoaded', () => {

    //------ Helper functions-------//
    function S(select) {
        return document.querySelector(select)
    }

    // Sleep() function
    function sleep(ms){
        return new Promise(resolve => setTimeout(resolve, ms))
    }

    // Convert to regular time
    function converTime(t){
        if (t < 13){
            return t + ':00 am'
        } else {
            return (t-12) + ':00 pm'
        }
    }

    function error_msg(msg){
        const content = `<div class="row justify-content-center alert alert-danger text-center">${msg}</div>`;
        S('#error-msg').innerHTML += content;
    }

    //------ Helper functions-------//


    // Sort the schedule times
    function sort(){
        var toSort = S('#sched-list').children;
        toSort = Array.prototype.slice.call(toSort, 0);

        toSort.sort(function(a, b) {
            var a_ord = +a.id.split('e')[1]; //id tags of the schedule items are timeINT the INT = the numeric time
            var b_ord = +b.id.split('e')[1]; //splitting at 'e' and getting the element at index 1 gives use the numeric time

            return (a_ord > b_ord) ? 1 : -1;
        });

        var parent = S('#sched-list');
        parent.innerHTML = "";

        for(var i = 0, l = toSort.length; i < l; i++) {
            parent.appendChild(toSort[i]);
        }
    }

    // Sends Ajax request to run the motor now versus waiting for a scheduled time
    S('#feednow').onclick = function() {
        // Change button style and text
        this.innerHTML = 'Feeding...';
        this.classList.remove('btn-success');
        this.classList.add('btn-grey');

        // Initialize new request
        const request = new XMLHttpRequest();
        request.open('POST', '/feed-now');

        // Callback function from when request completed
        request.onload = async () => {

              // Extact JSON data from request
              const data = JSON.parse(request.responseText);

              // Let user know request is completed
              if (data.success){
                  this.innerHTML = 'Complete!';
              }
              // sleep to give the user time to read the complete message
              await sleep(3000);

              // change text and styling back to original form
              this.innerHTML = "Feed Now";
              this.classList.remove('btn-grey');
              this.classList.add('btn-success');
        };
        request.send();
        return false;
    };

    //Adds time to schedule and displays them to user
    S('#sched-form').onsubmit = function() {

        // Initialize new request
        const request = new XMLHttpRequest();
        let e = S('#add-to-sched');
        let option = e.options[e.selectedIndex];
        let add_time = option.value;

        // If a disabled option is chosen chase the element to bring the users attention to is and return false
        if (option.getAttribute('value') === 'disabled-option'){
            e.style.removeProperty("WebkitAnimation");
            e.style.removeProperty("animation");

            e.style.WebkitAnimation = "shake .5s";
            e.style.animation = "shake .5s";
            return false
        }

        request.open('POST', '/add-to-schedule');

        //Callback function
        request.onload = () => {
            const data = JSON.parse(request.responseText);

            //Remove contents of the messages
            S('#error-msg').innerHTML = '';

            if (data.success){
                const content =
                    `
                      <div class="row justify-content-center" id="time${data.time}">
                         <div class="col-3 alert alert-success text-center m-0 p-1 rounded-0">
                            <i class="fas fa-lg fa-stopwatch"></i>
                        </div>
                         <div class="col-7 alert alert-success text-center font-weight-bold m-0 p-1 rounded-0">
                            ${converTime(data.time)}
                        </div>
                        <button class="col-2 btn btn-danger shadow-none text-center text-center m-0 p-1 rounded-0 border border-light delete-time" onclick="remove_time(${data.time})">
                            <i class="fas fa-lg fa-times"></i>
                        </button>
                      </div>
                    `;
                S('#sched-list').innerHTML += content;
                sort();
            } else {
                error_msg('This time is already scheduled.')
            }
        };

        // Add data to send with request
        const data = new FormData();
        data.append('add_time', add_time);

        //Send request
        request.send(data);
        return false;
    };
});