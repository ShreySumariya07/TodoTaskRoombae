import React,{ useState,useEffect } from 'react'
import {FaEdit,FaMonument,GiPentarrowsTornado,GiSaberToothedCatHead,ImCheckboxUnchecked, TiArrowMaximiseOutline, WiMoonAltWaxingGibbous1} from 'react-icons/all'
import moment from 'moment'
import axios from 'axios'
import './todo.css'
const Todo = () => {
    const[todo,setTodo] = useState([])
    const[task,setTask] = useState('')
    const[eta,setEta] = useState()

    // async function addTodo(){
    //     setTodo(
    //         {
    //             task:task,
    //             eta:eta,
    //             complete:false
    //         }
    //     )
    //     console.log("hello")
    //     axios({
    //         method:'post',
    //         url:'http://127.0.0.1:8000/createTodo/',
    //         data:todo
    //     }).then(function(response){
    //         console.log(response)
    //     })
        
        
    // }

    const addTodo = async () =>{

        const data = {
            task:task,
            eta:eta,
            complete:false
        }
        try{
            const response = await fetch("http://127.0.0.1:8000/createTodo/", {
                method: "POST",
                body : JSON.stringify(data),
                headers:{
                    "Content-Type": "application/json",
                    'Accept': 'application/json',
                    },
                })
            const res = await response.json()
            console.log(res)
        }
        catch(err){
            console.log(err)
        }
    }

    const getTodo = async() =>{
        try{
            const response = await fetch("http://127.0.0.1:8000/showTodo/",{
            method: "GET",
            })
            const res = await response.json()
            console.log(res)
            setTodo(res)
        }
        catch(err){
            console.log(err)
        }
    }

    useEffect(() => {
        getTodo()
    },[])
    const checkFunction = async (props) =>{
        const check = document.getElementById(`${props.id}`)
        if(check.checked === true){
            const data = {
                id:props.id,
                task:props.task,
                eta:props.eta,
                complete:true
            }
            console.log(data)
            try{
                const response = await fetch("http://127.0.0.1:8000/updateTodo/", {
                    method: "PUT",
                    body : JSON.stringify(data),
                    headers:{
                        "Content-Type": "application/json",
                        'Accept': 'application/json',
                        },
                    })
                const res = await response.json()
                console.log(res)
            }
            catch(err){
                console.log(err)
            }
        }
        else{
            console.log('world')
        }
    }
    return (
        <section className='section-center'>
                <h3>Todo</h3>
                <div className='form-control'>
                <input
                    type='text'
                    className='grocery'
                    placeholder='enter task'
                    value={task}
                    onChange={(e) => setTask(e.target.value)}
                />
                <input
                    type='date'
                    className='grocery'
                    placeholder='select date'
                    value={eta}
                    onChange={(e) => setEta(e.target.value)}
                />
                <button className='submit-btn' onClick={addTodo}>
                    submit
                </button>
                </div>
                <div className='grocery-list'>
                    {todo.map((todos) => {
                        console.log(todos)
                        console.log(moment(todos.eta).fromNow())
                        return (
                        <article className='grocery-item'>
                            <div>
                                <p className='title'>{todos.task}</p>
                            </div>
                            <div>
                                <p className='title'>{moment(todos.eta).fromNow()}</p>
                            </div>
                            <div className='btn-container'>
                                {todos.complete === true ? <input type="checkbox" id={todos.id} onClick={() => checkFunction(todos)} checked /> : <input type="checkbox" id={todos.id} onClick={() => checkFunction(todos)} />
                                }
                            </div>
                        </article>
                        );
                    })}
                </div>
        </section>
    )
}


export default Todo;