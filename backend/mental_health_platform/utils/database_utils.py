"""
Database utilities for mental health platform.
"""
from django.db import connection
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)


class DatabaseUtils:
    """Database utility functions."""
    
    @staticmethod
    def get_connection_info():
        """Get database connection information."""
        return {
            'engine': connection.vendor,
            'version': connection.get_server_version(),
            'database': connection.settings_dict['NAME']
        }
    
    @staticmethod
    def execute_raw_query(query, params=None):
        """Execute raw SQL query safely."""
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except Exception as e:
            logger.error(f"Database query error: {e}")
            return None
    
    @staticmethod
    def get_table_stats(table_name):
        """Get table statistics."""
        query = f"SELECT COUNT(*) FROM {table_name}"
        result = DatabaseUtils.execute_raw_query(query)
        return result[0][0] if result else 0
    
    @staticmethod
    def optimize_queries():
        """Optimize database queries."""
        with connection.cursor() as cursor:
            cursor.execute("ANALYZE")
            return True


class QueryOptimizer:
    """Query optimization utilities."""
    
    @staticmethod
    def filter_anonymized_data(queryset, user_field='user'):
        """Filter out personal data for analytics."""
        return queryset.filter(**{f'{user_field}__isnull': True})
    
    @staticmethod
    def get_aggregated_stats(queryset, group_by_field):
        """Get aggregated statistics."""
        return queryset.values(group_by_field).annotate(
            count=models.Count('id'),
            avg_value=models.Avg('value')
        )
    
    @staticmethod
    def paginate_queryset(queryset, page=1, page_size=20):
        """Paginate queryset efficiently."""
        start = (page - 1) * page_size
        end = start + page_size
        return queryset[start:end]


class DataValidator:
    """Data validation utilities."""
    
    @staticmethod
    def validate_email(email):
        """Validate email format."""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_phone(phone):
        """Validate phone number format."""
        import re
        pattern = r'^\+?1?\d{9,15}$'
        return re.match(pattern, phone) is not None
    
    @staticmethod
    def sanitize_text(text):
        """Sanitize text input."""
        import html
        return html.escape(text.strip())
