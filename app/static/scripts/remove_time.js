function remove_time(rem_time){
        const request = new XMLHttpRequest();
        request.open('POST', '/remove-time');

        request.onload = () => {

            //Remove contents of the messages
            document.querySelector('#error-msg').innerHTML = '';

            const data = JSON.parse(request.responseText);

            if(data.success){
               document.querySelector(`#time${rem_time}`).remove();
            } else {
               const content = `<div class="row justify-content-center alert alert-danger text-center">Error: Could not delete time.</div>`;
               document.querySelector('#error-msg').innerHTML += content;
            }
        };

        const data = new FormData();
        data.append('rem_time', rem_time);

        request.send(data);
        return false;
}