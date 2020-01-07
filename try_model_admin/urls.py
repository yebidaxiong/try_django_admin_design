"""try_model_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from GAS_Point_Interface.views import get_gas_realtime_data, get_gas_flag_data, get_gas_column_list
from Global_interface.views import search_online_point_dp_drawer, tabed_point_dp
from SIS_Point_Interface.views import get_sis_realtime_data, get_sis_flag_data, get_sis_column_list, \
    post_data_analysis_traffic_search, post_data_analysis_alarm_search
from try_model_admin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexrender),

    # restful api
    path('sis_realtime_data/', get_sis_realtime_data),
    path('sis_flag_data/', get_sis_flag_data),
    path('gas_realtime_data/', get_gas_realtime_data),
    path('gas_flag_data/', get_gas_flag_data),

    # for sis and gas get column name
    path('sis_column_list/', get_sis_column_list),
    path('gas_column_list/', get_gas_column_list),
    path('data_analysis_traffic_search/', post_data_analysis_traffic_search),
    path('data_analysis_alarm_search/', post_data_analysis_alarm_search),

    # for request for drawer from dynamic table in point monitor
    path('online_point_DT/', search_online_point_dp_drawer),
    path('tabed_point/', tabed_point_dp),
]
