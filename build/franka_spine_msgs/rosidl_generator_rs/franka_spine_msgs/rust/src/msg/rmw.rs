#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "franka_spine_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__franka_spine_msgs__msg__UserLimits() -> *const std::ffi::c_void;
}

#[link(name = "franka_spine_msgs__rosidl_generator_c")]
extern "C" {
    fn franka_spine_msgs__msg__UserLimits__init(msg: *mut UserLimits) -> bool;
    fn franka_spine_msgs__msg__UserLimits__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<UserLimits>, size: usize) -> bool;
    fn franka_spine_msgs__msg__UserLimits__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<UserLimits>);
    fn franka_spine_msgs__msg__UserLimits__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<UserLimits>, out_seq: *mut rosidl_runtime_rs::Sequence<UserLimits>) -> bool;
}

// Corresponds to franka_spine_msgs__msg__UserLimits
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// User-defined soft motion limits for the spine.

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct UserLimits {
    /// Lower motion limit
    pub lower_limit: f64,

    /// Upper motion limit
    pub upper_limit: f64,

}



impl Default for UserLimits {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !franka_spine_msgs__msg__UserLimits__init(&mut msg as *mut _) {
        panic!("Call to franka_spine_msgs__msg__UserLimits__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for UserLimits {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { franka_spine_msgs__msg__UserLimits__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { franka_spine_msgs__msg__UserLimits__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { franka_spine_msgs__msg__UserLimits__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for UserLimits {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for UserLimits where Self: Sized {
  const TYPE_NAME: &'static str = "franka_spine_msgs/msg/UserLimits";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__franka_spine_msgs__msg__UserLimits() }
  }
}


#[link(name = "franka_spine_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__franka_spine_msgs__msg__SpineParameters() -> *const std::ffi::c_void;
}

#[link(name = "franka_spine_msgs__rosidl_generator_c")]
extern "C" {
    fn franka_spine_msgs__msg__SpineParameters__init(msg: *mut SpineParameters) -> bool;
    fn franka_spine_msgs__msg__SpineParameters__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SpineParameters>, size: usize) -> bool;
    fn franka_spine_msgs__msg__SpineParameters__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SpineParameters>);
    fn franka_spine_msgs__msg__SpineParameters__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SpineParameters>, out_seq: *mut rosidl_runtime_rs::Sequence<SpineParameters>) -> bool;
}

// Corresponds to franka_spine_msgs__msg__SpineParameters
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// Aggregated spine parameters returned by the GetParameters service.

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SpineParameters {
    /// User-defined motion limits
    pub user_limits: super::super::msg::rmw::UserLimits,

}



impl Default for SpineParameters {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !franka_spine_msgs__msg__SpineParameters__init(&mut msg as *mut _) {
        panic!("Call to franka_spine_msgs__msg__SpineParameters__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SpineParameters {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { franka_spine_msgs__msg__SpineParameters__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { franka_spine_msgs__msg__SpineParameters__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { franka_spine_msgs__msg__SpineParameters__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SpineParameters {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SpineParameters where Self: Sized {
  const TYPE_NAME: &'static str = "franka_spine_msgs/msg/SpineParameters";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__franka_spine_msgs__msg__SpineParameters() }
  }
}


