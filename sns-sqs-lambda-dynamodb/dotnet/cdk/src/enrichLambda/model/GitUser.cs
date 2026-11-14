using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace enrichLambda.model
{
    
    internal class GitUser
    {
        public string login { get; set; } = "NoValue";
        public int id { get; set; } = 0;
        public string node_id { get; set; } = "NoValue";
        public string avatar_url { get; set; } = "NoValue";
        public string gravatar_id { get; set; } = "NoValue";
        public string url { get; set; } = "NoValue";
        public string html_url { get; set; } = "NoValue";
        public string followers_url { get; set; } = "NoValue";
        public string following_url { get; set; } = "NoValue";
        public string gists_url { get; set; } = "NoValue";
        public string starred_url { get; set; } = "NoValue";
        public string subscriptions_url { get; set; } = "NoValue";
        public string organizations_url { get; set; } = "NoValue";
        public string repos_url { get; set; } = "NoValue";
        public string events_url { get; set; } = "NoValue";
        public string received_events_url { get; set; } = "NoValue";
        public string type { get; set; } = "NoValue";
        public bool site_admin { get; set; } = false;
        public string name { get; set; } = "NoValue";
        public string company { get; set; } = "NoValue";
        public string blog { get; set; } = "NoValue";
        public string location { get; set; } = "NoValue";
        public string email { get; set; } = "NoValue";
        public string hireable { get; set; } = "NoValue";
        public string bio { get; set; } = "NoValue";
        public string twitter_username { get; set; } = "NoValue";
        public int public_repos { get; set; } = 0;
        public int public_gists { get; set; } = 0;
        public int followers { get; set; } = 0;
        public int following { get; set; } = 0;
        public DateTime created_at { get; set; } = DateTime.Now;
        public DateTime updated_at { get; set; } = DateTime.Now;
    }
}
