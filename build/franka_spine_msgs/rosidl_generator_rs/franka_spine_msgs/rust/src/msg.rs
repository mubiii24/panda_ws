#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to franka_spine_msgs__msg__UserLimits
/// User-defined soft motion limits for the spine.

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct UserLimits {
    /// Lower motion limit
    pub lower_limit: f64,

    /// Upper motion limit
    pub upper_limit: f64,

}



impl Default for UserLimits {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::UserLimits::default())
  }
}

impl rosidl_runtime_rs::Message for UserLimits {
  type RmwMsg = super::msg::rmw::UserLimits;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        lower_limit: msg.lower_limit,
        upper_limit: msg.upper_limit,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      lower_limit: msg.lower_limit,
      upper_limit: msg.upper_limit,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      lower_limit: msg.lower_limit,
      upper_limit: msg.upper_limit,
    }
  }
}


// Corresponds to franka_spine_msgs__msg__SpineParameters
/// Aggregated spine parameters returned by the GetParameters service.

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SpineParameters {
    /// User-defined motion limits
    pub user_limits: super::msg::UserLimits,

}



impl Default for SpineParameters {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::SpineParameters::default())
  }
}

impl rosidl_runtime_rs::Message for SpineParameters {
  type RmwMsg = super::msg::rmw::SpineParameters;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        user_limits: super::msg::UserLimits::into_rmw_message(std::borrow::Cow::Owned(msg.user_limits)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        user_limits: super::msg::UserLimits::into_rmw_message(std::borrow::Cow::Borrowed(&msg.user_limits)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      user_limits: super::msg::UserLimits::from_rmw_message(msg.user_limits),
    }
  }
}


