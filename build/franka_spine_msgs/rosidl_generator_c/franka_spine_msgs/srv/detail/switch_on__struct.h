// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from franka_spine_msgs:srv/SwitchOn.idl
// generated code does not contain a copyright notice

#ifndef FRANKA_SPINE_MSGS__SRV__DETAIL__SWITCH_ON__STRUCT_H_
#define FRANKA_SPINE_MSGS__SRV__DETAIL__SWITCH_ON__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/SwitchOn in the package franka_spine_msgs.
typedef struct franka_spine_msgs__srv__SwitchOn_Request
{
  uint8_t structure_needs_at_least_one_member;
} franka_spine_msgs__srv__SwitchOn_Request;

// Struct for a sequence of franka_spine_msgs__srv__SwitchOn_Request.
typedef struct franka_spine_msgs__srv__SwitchOn_Request__Sequence
{
  franka_spine_msgs__srv__SwitchOn_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} franka_spine_msgs__srv__SwitchOn_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'state'
// Member 'message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/SwitchOn in the package franka_spine_msgs.
typedef struct franka_spine_msgs__srv__SwitchOn_Response
{
  /// Spine state after switching on
  rosidl_runtime_c__String state;
  /// True if the transition succeeded
  bool success;
  /// Human-readable status or error description
  rosidl_runtime_c__String message;
} franka_spine_msgs__srv__SwitchOn_Response;

// Struct for a sequence of franka_spine_msgs__srv__SwitchOn_Response.
typedef struct franka_spine_msgs__srv__SwitchOn_Response__Sequence
{
  franka_spine_msgs__srv__SwitchOn_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} franka_spine_msgs__srv__SwitchOn_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FRANKA_SPINE_MSGS__SRV__DETAIL__SWITCH_ON__STRUCT_H_
