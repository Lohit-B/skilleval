const filter = (select_obj)=>{
    let category = select_obj.value
    if(!category || category== '') {
        return
    }
    window.location=`?category=${category}`
}
