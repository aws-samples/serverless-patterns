import { AppSyncResolverEvent } from 'aws-lambda'
const AWS = require('aws-sdk')
const {
  util: {
    uuid: { v4: uuid },
  },
} = AWS

type Todo = {
  id: string
  name: string
  description?: string
  createdAt: Date
  updatedAt: Date
}
const createdAt = new Date()
const todos: Todo[] = [
  { id: uuid(), name: 'first todo', createdAt, updatedAt: createdAt },
  { id: uuid(), name: 'second todo', createdAt, updatedAt: createdAt },
  { id: uuid(), name: 'third todo', createdAt, updatedAt: createdAt },
  { id: uuid(), name: 'fourth todo', createdAt, updatedAt: createdAt },
  { id: uuid(), name: 'fifth todo', createdAt, updatedAt: createdAt },
]

const getTodo = ({ id }: { id: string }) => todos.find((todo) => todo.id === id)

const listTodos = ({ limit }: { limit: number }) => ({ items: todos.slice(0, limit) })

type CreateTodoArgs = { id?: string; name: string; description?: string }
const createTodo = ({ id, name, description }: CreateTodoArgs) => {
  const createdAt = new Date()
  const todo: Todo = { id: id ?? uuid(), name, description, createdAt, updatedAt: createdAt }
  todos.push(todo)
  return todo
}

type UpdateTodoArgs = { id: string; name?: string; description?: string }
const updateTodo = ({ id, name, description }: UpdateTodoArgs) => {
  const index = todos.findIndex((todo) => todo.id === id)
  if (index < 0) return undefined
  const todo = todos[index]
  if (name) todo.name = name
  if (description) todo.description = description
  todo.updatedAt = new Date()
  todos[index] = todo
  return todo
}

const deleteTodo = ({ id }: { id: string }) => {
  const index = todos.findIndex((todo) => todo.id === id)
  if (index < 0) return undefined
  return todos.splice(index, 1)[0]
}

const operations: { [key: string]: { [key: string]: Function } } = {
  Query: { getTodo, listTodos },
  Mutation: { createTodo, updateTodo, deleteTodo },
}

exports.handler = async (event: AppSyncResolverEvent<{ [key: string]: string | number }>) => {
  console.log(`incoming event >`, JSON.stringify(event, null, 2))
  console.log(`todos >`, JSON.stringify(todos, null, 2))

  const {
    arguments: args,
    info: { parentTypeName: typeName, fieldName },
  } = event

  const type = operations[typeName]
  if (type) {
    const operation = type[fieldName]
    if (operation) {
      return operation(args)
    }
  }
  throw new Error('unknow operation')
}
