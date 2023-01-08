"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import collections.abc
import etcd3.rpc.rpc_pb2
import grpc

class KVStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Range: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.RangeRequest,
        etcd3.rpc.rpc_pb2.RangeResponse,
    ]
    """Range gets the keys in the range from the key-value store."""
    Put: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.PutRequest,
        etcd3.rpc.rpc_pb2.PutResponse,
    ]
    """Put puts the given key into the key-value store.
    A put request increments the revision of the key-value store
    and generates one event in the event history.
    """
    DeleteRange: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.DeleteRangeRequest,
        etcd3.rpc.rpc_pb2.DeleteRangeResponse,
    ]
    """DeleteRange deletes the given range from the key-value store.
    A delete request increments the revision of the key-value store
    and generates a delete event in the event history for every deleted key.
    """
    Txn: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.TxnRequest,
        etcd3.rpc.rpc_pb2.TxnResponse,
    ]
    """Txn processes multiple requests in a single transaction.
    A txn request increments the revision of the key-value store
    and generates events with the same revision for every completed request.
    It is not allowed to modify the same key several times within one txn.
    """
    Compact: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.CompactionRequest,
        etcd3.rpc.rpc_pb2.CompactionResponse,
    ]
    """Compact compacts the event history in the etcd key-value store. The key-value
    store should be periodically compacted or the event history will continue to grow
    indefinitely.
    """

class KVServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Range(
        self,
        request: etcd3.rpc.rpc_pb2.RangeRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.RangeResponse:
        """Range gets the keys in the range from the key-value store."""
    @abc.abstractmethod
    def Put(
        self,
        request: etcd3.rpc.rpc_pb2.PutRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.PutResponse:
        """Put puts the given key into the key-value store.
        A put request increments the revision of the key-value store
        and generates one event in the event history.
        """
    @abc.abstractmethod
    def DeleteRange(
        self,
        request: etcd3.rpc.rpc_pb2.DeleteRangeRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.DeleteRangeResponse:
        """DeleteRange deletes the given range from the key-value store.
        A delete request increments the revision of the key-value store
        and generates a delete event in the event history for every deleted key.
        """
    @abc.abstractmethod
    def Txn(
        self,
        request: etcd3.rpc.rpc_pb2.TxnRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.TxnResponse:
        """Txn processes multiple requests in a single transaction.
        A txn request increments the revision of the key-value store
        and generates events with the same revision for every completed request.
        It is not allowed to modify the same key several times within one txn.
        """
    @abc.abstractmethod
    def Compact(
        self,
        request: etcd3.rpc.rpc_pb2.CompactionRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.CompactionResponse:
        """Compact compacts the event history in the etcd key-value store. The key-value
        store should be periodically compacted or the event history will continue to grow
        indefinitely.
        """

def add_KVServicer_to_server(servicer: KVServicer, server: grpc.Server) -> None: ...

class WatchStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Watch: grpc.StreamStreamMultiCallable[
        etcd3.rpc.rpc_pb2.WatchRequest,
        etcd3.rpc.rpc_pb2.WatchResponse,
    ]
    """Watch watches for events happening or that have happened. Both input and output
    are streams; the input stream is for creating and canceling watchers and the output
    stream sends events. One watch RPC can watch on multiple key ranges, streaming events
    for several watches at once. The entire event history can be watched starting from the
    last compaction revision.
    """

class WatchServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Watch(
        self,
        request_iterator: collections.abc.Iterator[etcd3.rpc.rpc_pb2.WatchRequest],
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[etcd3.rpc.rpc_pb2.WatchResponse]:
        """Watch watches for events happening or that have happened. Both input and output
        are streams; the input stream is for creating and canceling watchers and the output
        stream sends events. One watch RPC can watch on multiple key ranges, streaming events
        for several watches at once. The entire event history can be watched starting from the
        last compaction revision.
        """

def add_WatchServicer_to_server(
    servicer: WatchServicer, server: grpc.Server
) -> None: ...

class LeaseStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    LeaseGrant: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.LeaseGrantRequest,
        etcd3.rpc.rpc_pb2.LeaseGrantResponse,
    ]
    """LeaseGrant creates a lease which expires if the server does not receive a keepAlive
    within a given time to live period. All keys attached to the lease will be expired and
    deleted if the lease expires. Each expired key generates a delete event in the event history.
    """
    LeaseRevoke: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.LeaseRevokeRequest,
        etcd3.rpc.rpc_pb2.LeaseRevokeResponse,
    ]
    """LeaseRevoke revokes a lease. All keys attached to the lease will expire and be deleted."""
    LeaseKeepAlive: grpc.StreamStreamMultiCallable[
        etcd3.rpc.rpc_pb2.LeaseKeepAliveRequest,
        etcd3.rpc.rpc_pb2.LeaseKeepAliveResponse,
    ]
    """LeaseKeepAlive keeps the lease alive by streaming keep alive requests from the client
    to the server and streaming keep alive responses from the server to the client.
    """
    LeaseTimeToLive: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.LeaseTimeToLiveRequest,
        etcd3.rpc.rpc_pb2.LeaseTimeToLiveResponse,
    ]
    """LeaseTimeToLive retrieves lease information."""
    LeaseLeases: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.LeaseLeasesRequest,
        etcd3.rpc.rpc_pb2.LeaseLeasesResponse,
    ]
    """LeaseLeases lists all existing leases."""

class LeaseServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def LeaseGrant(
        self,
        request: etcd3.rpc.rpc_pb2.LeaseGrantRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.LeaseGrantResponse:
        """LeaseGrant creates a lease which expires if the server does not receive a keepAlive
        within a given time to live period. All keys attached to the lease will be expired and
        deleted if the lease expires. Each expired key generates a delete event in the event history.
        """
    @abc.abstractmethod
    def LeaseRevoke(
        self,
        request: etcd3.rpc.rpc_pb2.LeaseRevokeRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.LeaseRevokeResponse:
        """LeaseRevoke revokes a lease. All keys attached to the lease will expire and be deleted."""
    @abc.abstractmethod
    def LeaseKeepAlive(
        self,
        request_iterator: collections.abc.Iterator[
            etcd3.rpc.rpc_pb2.LeaseKeepAliveRequest
        ],
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[etcd3.rpc.rpc_pb2.LeaseKeepAliveResponse]:
        """LeaseKeepAlive keeps the lease alive by streaming keep alive requests from the client
        to the server and streaming keep alive responses from the server to the client.
        """
    @abc.abstractmethod
    def LeaseTimeToLive(
        self,
        request: etcd3.rpc.rpc_pb2.LeaseTimeToLiveRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.LeaseTimeToLiveResponse:
        """LeaseTimeToLive retrieves lease information."""
    @abc.abstractmethod
    def LeaseLeases(
        self,
        request: etcd3.rpc.rpc_pb2.LeaseLeasesRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.LeaseLeasesResponse:
        """LeaseLeases lists all existing leases."""

def add_LeaseServicer_to_server(
    servicer: LeaseServicer, server: grpc.Server
) -> None: ...

class ClusterStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    MemberAdd: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.MemberAddRequest,
        etcd3.rpc.rpc_pb2.MemberAddResponse,
    ]
    """MemberAdd adds a member into the cluster."""
    MemberRemove: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.MemberRemoveRequest,
        etcd3.rpc.rpc_pb2.MemberRemoveResponse,
    ]
    """MemberRemove removes an existing member from the cluster."""
    MemberUpdate: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.MemberUpdateRequest,
        etcd3.rpc.rpc_pb2.MemberUpdateResponse,
    ]
    """MemberUpdate updates the member configuration."""
    MemberList: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.MemberListRequest,
        etcd3.rpc.rpc_pb2.MemberListResponse,
    ]
    """MemberList lists all the members in the cluster."""
    MemberPromote: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.MemberPromoteRequest,
        etcd3.rpc.rpc_pb2.MemberPromoteResponse,
    ]
    """MemberPromote promotes a member from raft learner (non-voting) to raft voting member."""

class ClusterServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def MemberAdd(
        self,
        request: etcd3.rpc.rpc_pb2.MemberAddRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.MemberAddResponse:
        """MemberAdd adds a member into the cluster."""
    @abc.abstractmethod
    def MemberRemove(
        self,
        request: etcd3.rpc.rpc_pb2.MemberRemoveRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.MemberRemoveResponse:
        """MemberRemove removes an existing member from the cluster."""
    @abc.abstractmethod
    def MemberUpdate(
        self,
        request: etcd3.rpc.rpc_pb2.MemberUpdateRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.MemberUpdateResponse:
        """MemberUpdate updates the member configuration."""
    @abc.abstractmethod
    def MemberList(
        self,
        request: etcd3.rpc.rpc_pb2.MemberListRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.MemberListResponse:
        """MemberList lists all the members in the cluster."""
    @abc.abstractmethod
    def MemberPromote(
        self,
        request: etcd3.rpc.rpc_pb2.MemberPromoteRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.MemberPromoteResponse:
        """MemberPromote promotes a member from raft learner (non-voting) to raft voting member."""

def add_ClusterServicer_to_server(
    servicer: ClusterServicer, server: grpc.Server
) -> None: ...

class MaintenanceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Alarm: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AlarmRequest,
        etcd3.rpc.rpc_pb2.AlarmResponse,
    ]
    """Alarm activates, deactivates, and queries alarms regarding cluster health."""
    Status: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.StatusRequest,
        etcd3.rpc.rpc_pb2.StatusResponse,
    ]
    """Status gets the status of the member."""
    Defragment: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.DefragmentRequest,
        etcd3.rpc.rpc_pb2.DefragmentResponse,
    ]
    """Defragment defragments a member's backend database to recover storage space."""
    Hash: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.HashRequest,
        etcd3.rpc.rpc_pb2.HashResponse,
    ]
    """Hash computes the hash of whole backend keyspace,
    including key, lease, and other buckets in storage.
    This is designed for testing ONLY!
    Do not rely on this in production with ongoing transactions,
    since Hash operation does not hold MVCC locks.
    Use "HashKV" API instead for "key" bucket consistency checks.
    """
    HashKV: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.HashKVRequest,
        etcd3.rpc.rpc_pb2.HashKVResponse,
    ]
    """HashKV computes the hash of all MVCC keys up to a given revision.
    It only iterates "key" bucket in backend storage.
    """
    Snapshot: grpc.UnaryStreamMultiCallable[
        etcd3.rpc.rpc_pb2.SnapshotRequest,
        etcd3.rpc.rpc_pb2.SnapshotResponse,
    ]
    """Snapshot sends a snapshot of the entire backend from a member over a stream to a client."""
    MoveLeader: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.MoveLeaderRequest,
        etcd3.rpc.rpc_pb2.MoveLeaderResponse,
    ]
    """MoveLeader requests current leader node to transfer its leadership to transferee."""
    Downgrade: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.DowngradeRequest,
        etcd3.rpc.rpc_pb2.DowngradeResponse,
    ]
    """Downgrade requests downgrades, verifies feasibility or cancels downgrade
    on the cluster version.
    Supported since etcd 3.5.
    """

class MaintenanceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Alarm(
        self,
        request: etcd3.rpc.rpc_pb2.AlarmRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AlarmResponse:
        """Alarm activates, deactivates, and queries alarms regarding cluster health."""
    @abc.abstractmethod
    def Status(
        self,
        request: etcd3.rpc.rpc_pb2.StatusRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.StatusResponse:
        """Status gets the status of the member."""
    @abc.abstractmethod
    def Defragment(
        self,
        request: etcd3.rpc.rpc_pb2.DefragmentRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.DefragmentResponse:
        """Defragment defragments a member's backend database to recover storage space."""
    @abc.abstractmethod
    def Hash(
        self,
        request: etcd3.rpc.rpc_pb2.HashRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.HashResponse:
        """Hash computes the hash of whole backend keyspace,
        including key, lease, and other buckets in storage.
        This is designed for testing ONLY!
        Do not rely on this in production with ongoing transactions,
        since Hash operation does not hold MVCC locks.
        Use "HashKV" API instead for "key" bucket consistency checks.
        """
    @abc.abstractmethod
    def HashKV(
        self,
        request: etcd3.rpc.rpc_pb2.HashKVRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.HashKVResponse:
        """HashKV computes the hash of all MVCC keys up to a given revision.
        It only iterates "key" bucket in backend storage.
        """
    @abc.abstractmethod
    def Snapshot(
        self,
        request: etcd3.rpc.rpc_pb2.SnapshotRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[etcd3.rpc.rpc_pb2.SnapshotResponse]:
        """Snapshot sends a snapshot of the entire backend from a member over a stream to a client."""
    @abc.abstractmethod
    def MoveLeader(
        self,
        request: etcd3.rpc.rpc_pb2.MoveLeaderRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.MoveLeaderResponse:
        """MoveLeader requests current leader node to transfer its leadership to transferee."""
    @abc.abstractmethod
    def Downgrade(
        self,
        request: etcd3.rpc.rpc_pb2.DowngradeRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.DowngradeResponse:
        """Downgrade requests downgrades, verifies feasibility or cancels downgrade
        on the cluster version.
        Supported since etcd 3.5.
        """

def add_MaintenanceServicer_to_server(
    servicer: MaintenanceServicer, server: grpc.Server
) -> None: ...

class AuthStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    AuthEnable: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthEnableRequest,
        etcd3.rpc.rpc_pb2.AuthEnableResponse,
    ]
    """AuthEnable enables authentication."""
    AuthDisable: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthDisableRequest,
        etcd3.rpc.rpc_pb2.AuthDisableResponse,
    ]
    """AuthDisable disables authentication."""
    AuthStatus: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthStatusRequest,
        etcd3.rpc.rpc_pb2.AuthStatusResponse,
    ]
    """AuthStatus displays authentication status."""
    Authenticate: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthenticateRequest,
        etcd3.rpc.rpc_pb2.AuthenticateResponse,
    ]
    """Authenticate processes an authenticate request."""
    UserAdd: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthUserAddRequest,
        etcd3.rpc.rpc_pb2.AuthUserAddResponse,
    ]
    """UserAdd adds a new user. User name cannot be empty."""
    UserGet: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthUserGetRequest,
        etcd3.rpc.rpc_pb2.AuthUserGetResponse,
    ]
    """UserGet gets detailed user information."""
    UserList: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthUserListRequest,
        etcd3.rpc.rpc_pb2.AuthUserListResponse,
    ]
    """UserList gets a list of all users."""
    UserDelete: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthUserDeleteRequest,
        etcd3.rpc.rpc_pb2.AuthUserDeleteResponse,
    ]
    """UserDelete deletes a specified user."""
    UserChangePassword: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthUserChangePasswordRequest,
        etcd3.rpc.rpc_pb2.AuthUserChangePasswordResponse,
    ]
    """UserChangePassword changes the password of a specified user."""
    UserGrantRole: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthUserGrantRoleRequest,
        etcd3.rpc.rpc_pb2.AuthUserGrantRoleResponse,
    ]
    """UserGrant grants a role to a specified user."""
    UserRevokeRole: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthUserRevokeRoleRequest,
        etcd3.rpc.rpc_pb2.AuthUserRevokeRoleResponse,
    ]
    """UserRevokeRole revokes a role of specified user."""
    RoleAdd: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthRoleAddRequest,
        etcd3.rpc.rpc_pb2.AuthRoleAddResponse,
    ]
    """RoleAdd adds a new role. Role name cannot be empty."""
    RoleGet: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthRoleGetRequest,
        etcd3.rpc.rpc_pb2.AuthRoleGetResponse,
    ]
    """RoleGet gets detailed role information."""
    RoleList: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthRoleListRequest,
        etcd3.rpc.rpc_pb2.AuthRoleListResponse,
    ]
    """RoleList gets lists of all roles."""
    RoleDelete: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthRoleDeleteRequest,
        etcd3.rpc.rpc_pb2.AuthRoleDeleteResponse,
    ]
    """RoleDelete deletes a specified role."""
    RoleGrantPermission: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthRoleGrantPermissionRequest,
        etcd3.rpc.rpc_pb2.AuthRoleGrantPermissionResponse,
    ]
    """RoleGrantPermission grants a permission of a specified key or range to a specified role."""
    RoleRevokePermission: grpc.UnaryUnaryMultiCallable[
        etcd3.rpc.rpc_pb2.AuthRoleRevokePermissionRequest,
        etcd3.rpc.rpc_pb2.AuthRoleRevokePermissionResponse,
    ]
    """RoleRevokePermission revokes a key or range permission of a specified role."""

class AuthServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def AuthEnable(
        self,
        request: etcd3.rpc.rpc_pb2.AuthEnableRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthEnableResponse:
        """AuthEnable enables authentication."""
    @abc.abstractmethod
    def AuthDisable(
        self,
        request: etcd3.rpc.rpc_pb2.AuthDisableRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthDisableResponse:
        """AuthDisable disables authentication."""
    @abc.abstractmethod
    def AuthStatus(
        self,
        request: etcd3.rpc.rpc_pb2.AuthStatusRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthStatusResponse:
        """AuthStatus displays authentication status."""
    @abc.abstractmethod
    def Authenticate(
        self,
        request: etcd3.rpc.rpc_pb2.AuthenticateRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthenticateResponse:
        """Authenticate processes an authenticate request."""
    @abc.abstractmethod
    def UserAdd(
        self,
        request: etcd3.rpc.rpc_pb2.AuthUserAddRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthUserAddResponse:
        """UserAdd adds a new user. User name cannot be empty."""
    @abc.abstractmethod
    def UserGet(
        self,
        request: etcd3.rpc.rpc_pb2.AuthUserGetRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthUserGetResponse:
        """UserGet gets detailed user information."""
    @abc.abstractmethod
    def UserList(
        self,
        request: etcd3.rpc.rpc_pb2.AuthUserListRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthUserListResponse:
        """UserList gets a list of all users."""
    @abc.abstractmethod
    def UserDelete(
        self,
        request: etcd3.rpc.rpc_pb2.AuthUserDeleteRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthUserDeleteResponse:
        """UserDelete deletes a specified user."""
    @abc.abstractmethod
    def UserChangePassword(
        self,
        request: etcd3.rpc.rpc_pb2.AuthUserChangePasswordRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthUserChangePasswordResponse:
        """UserChangePassword changes the password of a specified user."""
    @abc.abstractmethod
    def UserGrantRole(
        self,
        request: etcd3.rpc.rpc_pb2.AuthUserGrantRoleRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthUserGrantRoleResponse:
        """UserGrant grants a role to a specified user."""
    @abc.abstractmethod
    def UserRevokeRole(
        self,
        request: etcd3.rpc.rpc_pb2.AuthUserRevokeRoleRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthUserRevokeRoleResponse:
        """UserRevokeRole revokes a role of specified user."""
    @abc.abstractmethod
    def RoleAdd(
        self,
        request: etcd3.rpc.rpc_pb2.AuthRoleAddRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthRoleAddResponse:
        """RoleAdd adds a new role. Role name cannot be empty."""
    @abc.abstractmethod
    def RoleGet(
        self,
        request: etcd3.rpc.rpc_pb2.AuthRoleGetRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthRoleGetResponse:
        """RoleGet gets detailed role information."""
    @abc.abstractmethod
    def RoleList(
        self,
        request: etcd3.rpc.rpc_pb2.AuthRoleListRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthRoleListResponse:
        """RoleList gets lists of all roles."""
    @abc.abstractmethod
    def RoleDelete(
        self,
        request: etcd3.rpc.rpc_pb2.AuthRoleDeleteRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthRoleDeleteResponse:
        """RoleDelete deletes a specified role."""
    @abc.abstractmethod
    def RoleGrantPermission(
        self,
        request: etcd3.rpc.rpc_pb2.AuthRoleGrantPermissionRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthRoleGrantPermissionResponse:
        """RoleGrantPermission grants a permission of a specified key or range to a specified role."""
    @abc.abstractmethod
    def RoleRevokePermission(
        self,
        request: etcd3.rpc.rpc_pb2.AuthRoleRevokePermissionRequest,
        context: grpc.ServicerContext,
    ) -> etcd3.rpc.rpc_pb2.AuthRoleRevokePermissionResponse:
        """RoleRevokePermission revokes a key or range permission of a specified role."""

def add_AuthServicer_to_server(servicer: AuthServicer, server: grpc.Server) -> None: ...
