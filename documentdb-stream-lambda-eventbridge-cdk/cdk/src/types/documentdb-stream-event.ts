export interface DocumentDBStreamEvent {
  eventSourceArn: string
  events: DocumentDBEvent[]
  eventSource: string
}

export interface DocumentDBEvent {
  event: CdcEvent
}

export interface CdcEvent {
  _id: Id
  clusterTime: ClusterTime
  documentKey: DocumentKey
  fullDocument?: FullDocument
  ns: Ns
  operationType: 'insert' | 'update' | 'delete'
  updateDescription?: UpdateDescription
}

export interface Id {
  _data: string
}

export interface ClusterTime {
  $timestamp: Timestamp
}

export interface Timestamp {
  t: number
  i: number
}

export interface DocumentKey {
  _id: Id2
}

export interface Id2 {
  $oid: string
}

export interface FullDocument {
  _id: Id3
  [key: string]: any
}

export interface Id3 {
  $oid: string
}

export interface Ns {
  db: string
  coll: string
}

export interface UpdateDescription {
  removedFields: any[]
  truncatedArrays: any[]
  updatedFields: any
}
