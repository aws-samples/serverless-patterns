// Copyright 2023 klosep
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// 
//     http://www.apache.org/licenses/LICENSE-2.0
// 
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package software.amazon.samples.eventbridge;




public class KafkaPipeEvent {
    private int partition;
    private int offset;
    private long timestamp;
    private String timestampType;
    private String value;
    private String eventSourceArn;
    private String bootstrapServers;
    private String eventSource;
    private String eventSourceKey;
    private String topic;

    public KafkaPipeEvent() {}

    public String getTopic() {
        return topic;
    }

    public void setTopic(String topic) {
        this.topic = topic;
    }

    @Override
    public String toString() {
        return "KafkaPipeEvent{" +
                "partition=" + partition +
                ", offset=" + offset +
                ", timestamp=" + timestamp +
                ", timestampType='" + timestampType + '\'' +
                ", value='" + value + '\'' +
                ", eventSourceArn='" + eventSourceArn + '\'' +
                ", bootstrapServers='" + bootstrapServers + '\'' +
                ", eventSource='" + eventSource + '\'' +
                ", eventSourceKey='" + eventSourceKey + '\'' +
                '}';
    }

    public KafkaPipeEvent(int partition, int offset, long timestamp, String timestampType, String value, String eventSourceArn, String bootstrapServers, String eventSource, String eventSourceKey, String topic) {
        this.partition = partition;
        this.offset = offset;
        this.timestamp = timestamp;
        this.timestampType = timestampType;
        this.value = value;
        this.eventSourceArn = eventSourceArn;
        this.bootstrapServers = bootstrapServers;
        this.eventSource = eventSource;
        this.eventSourceKey = eventSourceKey;
        this.topic = topic;
    }

    public int getPartition() {
        return partition;
    }

    public void setPartition(int partition) {
        this.partition = partition;
    }

    public int getOffset() {
        return offset;
    }

    public void setOffset(int offset) {
        this.offset = offset;
    }

    public long getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(long timestamp) {
        this.timestamp = timestamp;
    }

    public String getTimestampType() {
        return timestampType;
    }

    public void setTimestampType(String timestampType) {
        this.timestampType = timestampType;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public String getEventSourceArn() {
        return eventSourceArn;
    }

    public void setEventSourceArn(String eventSourceArn) {
        this.eventSourceArn = eventSourceArn;
    }

    public String getBootstrapServers() {
        return bootstrapServers;
    }

    public void setBootstrapServers(String bootstrapServers) {
        this.bootstrapServers = bootstrapServers;
    }

    public String getEventSource() {
        return eventSource;
    }

    public void setEventSource(String eventSource) {
        this.eventSource = eventSource;
    }

    public String getEventSourceKey() {
        return eventSourceKey;
    }

    public void setEventSourceKey(String eventSourceKey) {
        this.eventSourceKey = eventSourceKey;
    }
}