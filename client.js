function valid() {
    fetch('/clientflag'). then (res => res.text()) .then(console.log);
}
