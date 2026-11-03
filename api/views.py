from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse


class about_me(View):

    def get(self,request):
        result={
            'id':235,
            'full_name':'Tony philip',
            'professional_title':'python developer',
            'bio':"superman",
            'email':"tonyphilip43@gmail.com",
            'contact':9061568050,
            'DOB':'07/10/2003',
            'github_url':"tony.url",
            'linkedin_url':'tony.link'
        }
        return JsonResponse(result)

class EducationMe(View):

    def get(self,request):
        result={
            'id':235,
            'institution':"luminar",
            'course':'python django',
            'university':"ktu",
            'location':"kasaragod",
            'start_yr':2022,
            'end_yr':2026,
            'CGPA':8.01,
            'Description':'unda'
        }
        return JsonResponse(result)

class ProjectsView(View):

    def get(self,request):
        content=[
            {
                'id':1,
                'title':'dietlense',
                'short_description':"AI powered food recognition",
                'long_description':"Built using gemini models and analyse",
                'technologies_used':['python','django','google_genai'],
                'live_url':'https://dietlense.example.com',
                'github_url':'https://github.com/yourusername/',
                'image_url':'https://api.yourdomain.com/media/project',
                'featured':True
            },
            {
                'id': 2,
                'title': 'Dental Clinic Management System',
                'short_description': 'Full-stack web application for managing a dental clinic',
                'long_description': 'A Django-based application for managing dentists, services, appointments, testimonials and gallery content through an admin panel.',
                'technologies_used': ['Python', 'Django', 'Django REST Framework', 'SQLite', 'React'],
                'live_url': 'https://dentalclinic.example.com',
                'github_url': 'https://github.com/yourusername/dental-clinic',
                'image_url': 'https://api.yourdomain.com/media/project/dental-clinic.jpg',
                'featured': True
            },

            {
                'id': 3,
                'title': 'Security Log Analyzer',
                'short_description': 'SIEM-based security log monitoring and analysis system',
                'long_description': 'A cybersecurity project for analyzing security logs, identifying suspicious activities and investigating alerts using SIEM concepts.',
                'technologies_used': ['Python', 'Wazuh', 'Grafana', 'SIEM', 'Windows Event Logs'],
                'live_url': 'https://securityanalyzer.example.com',
                'github_url': 'https://github.com/yourusername/security-log-analyzer',
                'image_url': 'https://api.yourdomain.com/media/project/security-analyzer.jpg',
                'featured': False
            }
        ]
        return JsonResponse(content,safe=False)

class SkillsView(View):

    def get(self,request):
        content=[
            {
                'id':1,
                'skill_name':'python',
                'Category':'Technical',
                'proficiency_level':'expert',
                'years_of_experience':1
            },
            {
                'id': 2,
                'skill_name': 'Django',
                'Category': 'Technical',
                'proficiency_level': 'intermediate',
                'years_of_experience': 1
            },

            {
                'id': 3,
                'skill_name': 'Cybersecurity',
                'Category': 'Security',
                'proficiency_level': 'intermediate',
                'years_of_experience': 1
            }
        ]
        return JsonResponse(content,safe=False)

class ExperienceView(View):

    def get(self,request):

        content = [

        {
            'id': 1,
            'job_title': 'Backend Developer',
            'company_name': 'TCS',
            'location': 'Kakkanad',
            'employment_type': 'Permanent',
            'start_date': '25/09/2026',
            'end_date': '25/09/2027',
            'currently_working': True,
            'description': 'Working on backend development using Python and Django.'
        },

        {
            'id': 2,
            'job_title': 'Python Developer Intern',
            'company_name': 'ABC Technologies',
            'location': 'Kochi',
            'employment_type': 'Internship',
            'start_date': '01/06/2025',
            'end_date': '31/08/2025',
            'currently_working': False,
            'description': 'Developed backend applications using Python and Django and worked with REST APIs.'
        },

        {
            'id': 3,
            'job_title': 'SOC Intern',
            'company_name': 'XYZ Cybersecurity',
            'location': 'Bangalore',
            'employment_type': 'Internship',
            'start_date': '02/02/2026',
            'end_date': '02/05/2026',
            'currently_working': False,
            'description': 'Analyzed security logs using Wazuh and Grafana and investigated security alerts.'
        }

        ]
        return JsonResponse(content,safe=False)

class CertificationView(View):

    def get(self, request):

        content = [

            {
                'id': 1,
                'certification_name': 'Python Programming Certification',
                'organization_name': 'Udemy',
                'issued_year': 2025
            },

            {
                'id': 2,
                'certification_name': 'Django Web Development Certification',
                'organization_name': 'Coursera',
                'issued_year': 2025
            },

            {
                'id': 3,
                'certification_name': 'Cybersecurity Fundamentals Certification',
                'organization_name': 'Cisco',
                'issued_year': 2026
            }

        ]

        return JsonResponse(content, safe=False)

class ServicesView(View):

    def get(self, request):

        content = [

            {
                'id': 1,
                'service_name': 'Backend Development',
                'description': 'Building scalable and secure backend applications using Python and Django.',
                'technologies': ['Python', 'Django', 'Django REST Framework']
            },

            {
                'id': 2,
                'service_name': 'Web Development',
                'description': 'Developing responsive and user-friendly websites and web applications.',
                'technologies': ['HTML', 'CSS', 'JavaScript', 'React']
            },

            {
                'id': 3,
                'service_name': 'Cybersecurity',
                'description': 'Security monitoring, log analysis and threat detection for applications and systems.',
                'technologies': ['Wazuh', 'Grafana', 'SIEM', 'Wireshark']
            }

        ]

        return JsonResponse(content, safe=False)