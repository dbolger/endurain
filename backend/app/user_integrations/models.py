from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Boolean,
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import JSON
from database import Base


class UserIntegrations(Base):
    __tablename__ = "users_integrations"

    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="User ID that the integration belongs",
    )
    strava_state = Column(String(length=45), default=None, nullable=True)
    strava_token = Column(String(length=250), default=None, nullable=True)
    strava_refresh_token = Column(String(length=250), default=None, nullable=True)
    strava_token_expires_at = Column(DateTime, default=None, nullable=True)
    strava_sync_gear = Column(
        Boolean,
        nullable=False,
        default=False,
        comment="Whether Strava gear is to be synced",
    )
    garminconnect_oauth1 = Column(
        JSON, default=None, nullable=True, doc="Garmin OAuth1 token"
    )
    garminconnect_oauth2 = Column(
        JSON, default=None, nullable=True, doc="Garmin OAuth2 token"
    )
    garminconnect_sync_gear = Column(
        Boolean,
        nullable=False,
        default=False,
        comment="Whether Garmin Connect gear is to be synced",
    )

    # Define a relationship to the User model
    user = relationship("User", back_populates="users_integrations")
