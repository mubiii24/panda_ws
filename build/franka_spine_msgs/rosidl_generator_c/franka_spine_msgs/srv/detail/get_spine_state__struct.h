// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from franka_spine_msgs:srv/GetSpineState.idl
// generated code does not contain a copyright notice

#ifndef FRANKA_SPINE_MSGS__SRV__DETAIL__GET_SPINE_STATE__STRUCT_H_
#define FRANKA_SPINE_MSGS__SRV__DETAIL__GET_SPINE_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/GetSpineState in the package franka_spine_msgs.
typedef struct franka_spine_msgs__srv__GetSpineState_Request
{
  uint8_t structure_needs_at_least_one_member;
} franka_spine_msgs__srv__GetSpineState_Request;

// Struct for a sequence of franka_spine_msgs__srv__GetSpineState_Request.
typedef struct franka_spine_msgs__srv__GetSpineState_Request__Sequence
{
  franka_spine_msgs__srv__GetSpineState_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} franka_spine_msgs__srv__GetSpineState_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'state'
// Member 'error_code'
// Member 'error_description'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/GetSpineState in the package franka_spine_msgs.
typedef struct franka_spine_msgs__srv__GetSpineState_Response
{
  /// Current spine state
  rosidl_runtime_c__String state;
  /// Error code (empty when no error)
  rosidl_runtime_c__String error_code;
  /// Human-readable error description
  rosidl_runtime_c__String error_description;
  /// True if the REST call succeeded
  bool success;
} franka_spine_msgs__srv__GetSpineState_Response;

// Struct for a sequence of franka_spine_msgs__srv__GetSpineState_Response.
typedef struct franka_spine_msgs__srv__GetSpineState_Response__Sequence
{
  franka_spine_msgs__srv__GetSpineState_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} franka_spine_msgs__srv__GetSpineState_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FRANKA_SPINE_MSGS__SRV__DETAIL__GET_SPINE_STATE__STRUCT_H_
