"""
Example aerospace computing module
This file demonstrates basic aerospace calculations
"""

def calculate_orbital_velocity(radius, gravitational_parameter=3.986e14):
    """
    Calculate orbital velocity for a circular orbit
    
    Args:
        radius: Orbital radius in meters
        gravitational_parameter: Standard gravitational parameter (m³/s²)
    
    Returns:
        Orbital velocity in m/s
    """
    return (gravitational_parameter / radius) ** 0.5


def calculate_escape_velocity(radius, gravitational_parameter=3.986e14):
    """
    Calculate escape velocity from a celestial body
    
    Args:
        radius: Distance from center of body in meters
        gravitational_parameter: Standard gravitational parameter (m³/s²)
    
    Returns:
        Escape velocity in m/s
    """
    return (2 * gravitational_parameter / radius) ** 0.5


if __name__ == "__main__":
    # Example: Calculate orbital velocity at ISS altitude
    earth_radius = 6371000  # meters
    iss_altitude = 408000  # meters
    iss_orbital_radius = earth_radius + iss_altitude
    
    orbital_vel = calculate_orbital_velocity(iss_orbital_radius)
    print(f"ISS Orbital Velocity: {orbital_vel:.2f} m/s ({orbital_vel/1000:.2f} km/s)")
    
    escape_vel = calculate_escape_velocity(iss_orbital_radius)
    print(f"Escape Velocity at ISS altitude: {escape_vel:.2f} m/s ({escape_vel/1000:.2f} km/s)")
