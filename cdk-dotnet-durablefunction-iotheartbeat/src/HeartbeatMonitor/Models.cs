using System.Diagnostics.CodeAnalysis;

namespace HeartbeatMonitor;

/// <summary>
/// Input to the heartbeat monitor workflow.
/// Contains the device ID to monitor and configuration for timeouts.
/// </summary>
[SuppressMessage("Performance", "CA1812:Avoid uninstantiated internal classes", Justification = "Deserialized by Lambda runtime")]
internal sealed record MonitorInput(
    string DeviceId,
    int HeartbeatTimeoutSeconds = 60,
    int MaxCyclesBeforeRestart = 100);

/// <summary>
/// State carried across monitoring cycles within a single execution.
/// </summary>
internal sealed record MonitorState(
    string DeviceId,
    int CycleCount,
    int MissedHeartbeats,
    string Status,
    DateTime LastHeartbeatAt,
    DateTime StartedAt);

/// <summary>
/// A heartbeat signal stored in DynamoDB by the receiver.
/// </summary>
internal sealed record HeartbeatRecord(
    string DeviceId,
    DateTime Timestamp,
    string Status);

/// <summary>
/// Result returned when the monitor restarts (continue-as-new).
/// </summary>
internal sealed record MonitorResult(
    string DeviceId,
    string Reason,
    int CompletedCycles,
    DateTime RestartedAt);
